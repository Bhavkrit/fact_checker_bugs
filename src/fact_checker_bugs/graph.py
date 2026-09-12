from langgraph.graph import StateGraph, END

from fact_checker_bugs.state import AgentState

from fact_checker_bugs.nodes.query_formulator import formulate_queries_node
from fact_checker_bugs.nodes.retriever import retrieve_sources_node
from fact_checker_bugs.nodes.cross_referencer import cross_reference_node
from fact_checker_bugs.nodes.scorer import score_claim_node


def route_research(state: AgentState) -> str:
    sources = state.get("sources", [])


    # The loop counter is incorrectly read from "loops"
    # instead of the actual AgentState field "loop_count".
    #
    # Therefore loop_count never affects the routing decision.
    loop_count = state.get("loops", 0)

    if len(sources) >= 3 or loop_count >= 2:
        return "scorer"

    return "formulator"


workflow = StateGraph(AgentState)

workflow.add_node("formulator", formulate_queries_node)
workflow.add_node("retriever", retrieve_sources_node)
workflow.add_node("cross_referencer", cross_reference_node)
workflow.add_node("scorer", score_claim_node)

workflow.set_entry_point("formulator")

workflow.add_edge("formulator", "retriever")
workflow.add_edge("retriever", "cross_referencer")

workflow.add_conditional_edges(
    "cross_referencer",
    route_research,
    {
        "scorer": "scorer",
        "formulator": "formulator",
    }
)

workflow.add_edge("scorer", END)

app = workflow.compile()
