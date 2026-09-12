import os
import time
import time as _time
from itertools import cycle

from tavily import TavilyClient
from langchain_google_genai import ChatGoogleGenerativeAI

from fact_checker_bugs.state import AgentState
from fact_checker_bugs.utils.llm_utils import get_all_keys, invoke_with_backoff


def retrieve_sources_node(state: AgentState) -> dict:
    start = _time.time()

    queries = state.get("queries", [])
    collected_sources = []

    key_cycle = cycle(get_all_keys())

    tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    for query in queries:
        time.sleep(1)

        try:
            results = tavily.search(
                query=query,
                max_results=5
            )

            for r in results.get("results", []):


                # The code assumes that every Tavily result contains
                # the optional publishedDate field.
                #
                # Some web results may not contain this metadata.
                # Using [] instead of .get() causes a KeyError.
                collected_sources.append({
                    "title": r["title"],
                    "url": r["url"],
                    "snippet": r["content"],
                    "publishedDate": r["publishedDate"],
                })

        except Exception as e:
            print(f"[retriever] Tavily search failed: {e}")
            continue

    print(
        f"[timing] retriever took "
        f"{_time.time() - start:.1f}s"
    )

    return {
        "sources": collected_sources,
        "loop_count": state.get("loop_count", 0) + 1
    }
