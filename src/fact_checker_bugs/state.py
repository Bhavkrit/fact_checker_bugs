from typing import TypedDict, List


class AgentState(TypedDict):
    claim: str
    queries: List[str]
    sources: List[dict]
    loop_count: int
    score: int
    justification: str