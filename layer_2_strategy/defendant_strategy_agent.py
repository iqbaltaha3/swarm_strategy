from core.llm import call_structured
from core.state import StrategyState
from .schemas import DefendantStrategy
from .prompts import DEFENDANT_SYSTEM, DEFENDANT_USER


def run_defendant_strategy(state: StrategyState) -> dict:
    """Layer 2: Defendant strategy"""
    analysis = str(state.get("battlefield_analysis", ""))
    result = call_structured(
        system_prompt=DEFENDANT_SYSTEM,
        user_prompt=DEFENDANT_USER.format(analysis=analysis),
        schema=DefendantStrategy,
        agent_name="defendant_strategy",
    )
    return {"defendant_strategy": result}
