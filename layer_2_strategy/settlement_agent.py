from core.llm import call_structured
from core.state import StrategyState
from .schemas import SettlementFramework
from .prompts import SETTLEMENT_SYSTEM, SETTLEMENT_USER


def run_settlement(state: StrategyState) -> dict:
    """Layer 2: Settlement strategy"""
    analysis = str(state.get("battlefield_analysis", ""))
    result = call_structured(
        system_prompt=SETTLEMENT_SYSTEM,
        user_prompt=SETTLEMENT_USER.format(analysis=analysis),
        schema=SettlementFramework,
        agent_name="settlement",
    )
    return {"settlement": result}
