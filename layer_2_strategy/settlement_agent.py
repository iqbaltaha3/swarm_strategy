from constitution.loader import inject_constitution_into_prompt
from core.llm import call_structured
from core.state import StrategyState
from .schemas import SettlementFramework
from .prompts import SETTLEMENT_SYSTEM, SETTLEMENT_USER


def run_settlement(state: StrategyState) -> dict:
    """Layer 2: Settlement strategy"""
    analysis = str(state.get("battlefield_analysis", ""))
    system_prompt = inject_constitution_into_prompt(
        SETTLEMENT_SYSTEM,
        "settlement",
    )

    result = call_structured(
        system_prompt=system_prompt,
        user_prompt=SETTLEMENT_USER.format(analysis=analysis),
        schema=SettlementFramework,
    )
    return {"settlement": result}
