from constitution.loader import inject_constitution_into_prompt
from core.llm import call_structured
from core.state import StrategyState
from .schemas import PlaintiffStrategy
from .prompts import PLAINTIFF_SYSTEM, PLAINTIFF_USER


def run_plaintiff_strategy(state: StrategyState) -> dict:
    """Layer 2: Plaintiff strategy"""
    analysis = str(state.get("battlefield_analysis", ""))
    system_prompt = inject_constitution_into_prompt(
        PLAINTIFF_SYSTEM,
        "plaintiff_strategy",
    )

    result = call_structured(
        system_prompt=system_prompt,
        user_prompt=PLAINTIFF_USER.format(analysis=analysis),
        schema=PlaintiffStrategy,
    )
    return {"plaintiff_strategy": result}
