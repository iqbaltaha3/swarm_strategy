from core.llm import call_structured
from core.state import StrategyState
from .schemas import PlaintiffStrategy
from .prompts import PLAINTIFF_SYSTEM, PLAINTIFF_USER


def run_plaintiff_strategy(state: StrategyState) -> dict:
    """Layer 2: Plaintiff strategy"""
    analysis = str(state.get("battlefield_analysis", ""))
    result = call_structured(
        system_prompt=PLAINTIFF_SYSTEM,
        user_prompt=PLAINTIFF_USER.format(analysis=analysis),
        schema=PlaintiffStrategy,
    )
    return {"plaintiff_strategy": result}
