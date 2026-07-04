from constitution.loader import inject_constitution_into_prompt
from core.llm import call_structured
from core.state import StrategyState
from .schemas import RiskAnalysis
from .prompts import RISK_SYSTEM, RISK_USER


def run_risk_assessment(state: StrategyState) -> dict:
    """Layer 2: Risk assessment"""
    analysis = str(state.get("battlefield_analysis", ""))
    system_prompt = inject_constitution_into_prompt(
        RISK_SYSTEM,
        "risk_assessment",
    )

    result = call_structured(
        system_prompt=system_prompt,
        user_prompt=RISK_USER.format(analysis=analysis),
        schema=RiskAnalysis,
    )
    return {"risk_analysis": result}
