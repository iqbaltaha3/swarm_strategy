from constitution.loader import inject_constitution_into_prompt
from core.llm import call_structured
from core.state import StrategyState
from .schemas import BattlefieldAnalysis
from .prompts import BATTLEFIELD_SYSTEM, BATTLEFIELD_USER


def run_battlefield_understanding(state: StrategyState) -> dict:
    """Layer 1: Analyze case fundamentals"""
    
    complaint = state.get("complaint", "")
    
    system_prompt = inject_constitution_into_prompt(
        BATTLEFIELD_SYSTEM,
        "battlefield_understanding",
    )

    result = call_structured(
        system_prompt=system_prompt,
        user_prompt=BATTLEFIELD_USER.format(complaint=complaint),
        schema=BattlefieldAnalysis,
    )
    
    return {"battlefield_analysis": result}
