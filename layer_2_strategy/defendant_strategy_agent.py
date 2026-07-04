from constitution.loader import inject_constitution_into_prompt
from core.llm import call_structured
from core.state import StrategyState
from .schemas import DefendantStrategy
from .prompts import DEFENDANT_SYSTEM, DEFENDANT_USER


def run_defendant_strategy(state: StrategyState) -> dict:
    """Layer 2: Defendant strategy"""
    analysis = str(state.get("battlefield_analysis", ""))
    system_prompt = inject_constitution_into_prompt(
        DEFENDANT_SYSTEM,
        "defendant_strategy",
    )

    result = call_structured(
        system_prompt=system_prompt,
        user_prompt=DEFENDANT_USER.format(analysis=analysis),
        schema=DefendantStrategy,
    )
    return {"defendant_strategy": result}
