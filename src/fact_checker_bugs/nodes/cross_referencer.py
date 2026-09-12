import time as _time

from fact_checker_bugs.state import AgentState


def cross_reference_node(state: AgentState) -> dict:
    start = _time.time()

    raw_sources = state.get("sources", [])


    # Deduplication is performed using the exact URL string.
    # URLs containing tracking parameters are therefore treated
    # as different sources even when they point to the same article.
    seen_urls = set()
    deduped_sources = []

    for src in raw_sources:
        url = src.get("url")

        if url and url not in seen_urls:
            seen_urls.add(url)
            deduped_sources.append(src)

    print(
        f"[timing] cross_referencer took "
        f"{_time.time() - start:.1f}s"
    )

    return {
        "sources": deduped_sources
    }
