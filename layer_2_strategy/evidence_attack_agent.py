from constitution.loader import inject_constitution_into_prompt
from core.llm import call_structured
from core.state import StrategyState
from .schemas import EvidenceAttack
from .prompts import EVIDENCE_SYSTEM, EVIDENCE_USER


def run_evidence_attack(state: StrategyState) -> dict:
    """Layer 2: Evidence attack analysis"""
    analysis = str(state.get("battlefield_analysis", ""))
    system_prompt = inject_constitution_into_prompt(
        EVIDENCE_SYSTEM,
        "evidence_attack",
    )

    result = call_structured(
        system_prompt=system_prompt,
        user_prompt=EVIDENCE_USER.format(analysis=analysis),
        schema=EvidenceAttack,
    )
    return {"evidence_attack": result}
