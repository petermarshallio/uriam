"""Chat-completion clients for the profiling harness.

Both providers expose the same interface -- send(messages, system, on_progress)
-> Reply -- so run.py doesn't need to know which one it's talking to. Both
stream internally: on_progress(text_so_far) fires as content arrives, which is
what lets the caller show live progress instead of a frozen spinner during a
slow generation, and (for Ollama) is what makes a genuinely dead server show
up immediately as a stalled stream rather than needing a separate health check.
"""

from __future__ import annotations

import json
from typing import Callable, NamedTuple, Optional

import anthropic
import requests

# Comfortably under every current model's real ceiling (Haiku caps at 64K
# output, everything else at 128K) -- high enough that a batched, multi-part
# section reply essentially never gets cut off. Costs nothing extra unless a
# model actually needs it: Anthropic bills for tokens generated, not for this
# ceiling. Now that both providers stream, there's no timeout reason to keep
# it low either.
DEFAULT_MAX_TOKENS = 32000
OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"
OLLAMA_TIMEOUT_SECONDS = 600
# Ollama defaults to a 2048-token context window regardless of what the model
# actually supports -- far too small for an accumulating multi-section
# conversation. Left unset, it doesn't error when exceeded; it silently
# discards earlier context ("context shift") instead, so the model quietly
# stops seeing turns it needs. Every model currently in models.yaml supports
# well beyond this.
OLLAMA_NUM_CTX = 16384

ProgressCallback = Optional[Callable[[str], None]]


class Reply(NamedTuple):
    text: str
    truncated: bool
    input_tokens: int
    output_tokens: int


class OllamaUnavailableError(RuntimeError):
    """The Ollama service itself can't be reached, or stopped responding mid-stream."""


class OllamaModelNotFoundError(RuntimeError):
    """The service is up, but the requested model tag isn't pulled locally."""


class AnthropicProvider:
    def __init__(self, model: str):
        self.model = model
        self._client = anthropic.Anthropic()

    def send(self, messages: list[dict], system: str, on_progress: ProgressCallback = None) -> Reply:
        accumulated = ""
        with self._client.messages.stream(
            model=self.model,
            max_tokens=DEFAULT_MAX_TOKENS,
            system=system,
            messages=messages,
        ) as stream:
            for delta in stream.text_stream:
                accumulated += delta
                if on_progress:
                    on_progress(accumulated)
            response = stream.get_final_message()

        text = "".join(block.text for block in response.content if block.type == "text")
        return Reply(
            text=text,
            truncated=response.stop_reason == "max_tokens",
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
        )


class OllamaProvider:
    def __init__(self, model: str):
        self.model = model

    def send(self, messages: list[dict], system: str, on_progress: ProgressCallback = None) -> Reply:
        payload_messages = [{"role": "system", "content": system}, *messages]
        try:
            response = requests.post(
                OLLAMA_CHAT_URL,
                json={
                    "model": self.model,
                    "messages": payload_messages,
                    "stream": True,
                    "options": {"num_ctx": OLLAMA_NUM_CTX},
                },
                timeout=OLLAMA_TIMEOUT_SECONDS,
                stream=True,
            )
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as exc:
            raise OllamaUnavailableError(
                f"Can't reach Ollama at {OLLAMA_CHAT_URL} -- is it running? Try: ollama serve"
            ) from exc

        if response.status_code == 404:
            detail = ""
            if response.content:
                try:
                    detail = f" ({response.json().get('error', response.text)})"
                except ValueError:
                    detail = f" ({response.text})"
            raise OllamaModelNotFoundError(
                f"'{self.model}' isn't pulled -- try: ollama pull {self.model}{detail}"
            )
        response.raise_for_status()

        accumulated = ""
        final_data: dict = {}
        try:
            for line in response.iter_lines():
                if not line:
                    continue
                data = json.loads(line)
                chunk = data.get("message", {}).get("content", "")
                if chunk:
                    accumulated += chunk
                    if on_progress:
                        on_progress(accumulated)
                if data.get("done"):
                    final_data = data
        except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError) as exc:
            raise OllamaUnavailableError(
                f"Ollama connection dropped mid-response after {len(accumulated)} chars -- is the service still up?"
            ) from exc

        return Reply(
            text=accumulated,
            truncated=final_data.get("done_reason") == "length",
            input_tokens=final_data.get("prompt_eval_count", 0),
            output_tokens=final_data.get("eval_count", 0),
        )


def get_provider(provider: str, model: str) -> AnthropicProvider | OllamaProvider:
    if provider == "anthropic":
        return AnthropicProvider(model)
    if provider == "ollama":
        return OllamaProvider(model)
    raise ValueError(f"Unknown provider: {provider!r}")
