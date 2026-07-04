from core.llm import call_structured
from core.state import StrategyState
from .schemas import StrategyJudgment, RecommendedPath
from .prompts import JUDGE_SYSTEM, JUDGE_USER, PATH_SYSTEM, PATH_USER


def run_strategy_judge(state: StrategyState) -> dict:
    """Layer 3: Judge all strategies, assess probabilities, and recommend approach"""
    
    plaintiff = str(state.get("plaintiff_strategy", ""))
    defendant = str(state.get("defendant_strategy", ""))
    evidence = str(state.get("evidence_attack", ""))
    risk = str(state.get("risk_analysis", ""))
    settlement = str(state.get("settlement", ""))
    
    result = call_structured(
        system_prompt=JUDGE_SYSTEM,
        user_prompt=JUDGE_USER.format(
            plaintiff=plaintiff,
            defendant=defendant,
            evidence=evidence,
            risk=risk,
            settlement=settlement,
        ),
        schema=StrategyJudgment,
        agent_name="judge",
    )
    
    return {"strategy_judgment": result}


def run_recommended_path(state: StrategyState) -> dict:
    """Layer 3: Recommend strategic path forward based on judgment"""
    
    battlefield = str(state.get("battlefield_analysis", ""))
    judge = str(state.get("strategy_judgment", ""))
    
    result = call_structured(
        system_prompt=PATH_SYSTEM,
        user_prompt=PATH_USER.format(
            battlefield=battlefield,
            judge=judge,
        ),
        schema=RecommendedPath,
        agent_name="recommended_path",
    )
    
    return {"recommended_path": result}
