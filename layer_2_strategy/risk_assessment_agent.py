from core.llm import call_structured
from core.state import StrategyState
from .schemas import RiskAnalysis
from .prompts import RISK_SYSTEM, RISK_USER


def run_risk_assessment(state: StrategyState) -> dict:
    """Layer 2: Risk assessment"""
    analysis = str(state.get("battlefield_analysis", ""))
    result = call_structured(
        system_prompt=RISK_SYSTEM,
        user_prompt=RISK_USER.format(analysis=analysis),
        schema=RiskAnalysis,
        agent_name="risk_assessment",
    )
    return {"risk_analysis": result}
