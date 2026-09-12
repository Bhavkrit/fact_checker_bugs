import os
import random
import time

def _is_rate_limit_error(exc: BaseException) -> bool:
    msg = str(exc)
    return "429" in msg or "ResourceExhausted" in type(exc).__name__ or "quota" in msg.lower()

def get_all_keys():
    keys = [os.getenv(f"GEMINI_API_KEY_{i}") for i in [1, 2, 3]]
    valid = [k for k in keys if k]
    fallback = os.getenv("GEMINI_API_KEY")
    if fallback and fallback not in valid:
        valid.append(fallback)
    if not valid:
        raise RuntimeError("No Gemini API keys found in environment.")
    random.shuffle(valid)
    return valid

def invoke_with_backoff(build_llm_fn, prompt, max_attempts=3, base_delay=2):
    """
    build_llm_fn: no-arg callable returning a fresh llm bound to the next key.
    Retries on 429s with exponential backoff, rotating keys each attempt.
    """
    last_exc = None
    for attempt in range(max_attempts):
        try:
            llm = build_llm_fn()
            return llm.invoke(prompt)
        except Exception as e:
            last_exc = e
            if _is_rate_limit_error(e) and attempt < max_attempts - 1:
                delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                print(f"[retry] 429 hit, waiting {delay:.1f}s (attempt {attempt+1}/{max_attempts})")
                time.sleep(delay)
                continue
            raise
    raise last_exc