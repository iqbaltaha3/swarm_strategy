from core.llm import call_structured
from core.state import StrategyState
from .schemas import BattlefieldAnalysis
from .prompts import BATTLEFIELD_SYSTEM, BATTLEFIELD_USER


def run_battlefield_understanding(state: StrategyState) -> dict:
    """Layer 1: Analyze case fundamentals"""
    
    complaint = state.get("complaint", "")
    
    result = call_structured(
        system_prompt=BATTLEFIELD_SYSTEM,
        user_prompt=BATTLEFIELD_USER.format(complaint=complaint),
        schema=BattlefieldAnalysis,
        agent_name="battlefield_understanding",
    )
    
    return {"battlefield_analysis": result}
