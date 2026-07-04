from langgraph.graph import StateGraph, END

from core.state import StrategyState

# Layer 1: Battlefield Understanding
from layer_1_understanding.battlefield_understanding_agent import run_battlefield_understanding

# Layer 2: Specialized Strategies
from layer_2_strategy.plaintiff_strategy_agent import run_plaintiff_strategy
from layer_2_strategy.defendant_strategy_agent import run_defendant_strategy
from layer_2_strategy.evidence_attack_agent import run_evidence_attack
from layer_2_strategy.risk_assessment_agent import run_risk_assessment
from layer_2_strategy.settlement_agent import run_settlement

# Layer 3: Coordination & Judgment
from layer_3_coordination.judge_agent import (
    run_strategy_judge,
    run_recommended_path,
)

builder = StateGraph(StrategyState)

# =====================================================
# LAYER 1: BATTLEFIELD UNDERSTANDING
# =====================================================
builder.add_node("battlefield_understanding", run_battlefield_understanding)

# =====================================================
# LAYER 2: SPECIALIZED STRATEGIES (Parallel)
# =====================================================
builder.add_node("plaintiff_strategy", run_plaintiff_strategy)
builder.add_node("defendant_strategy", run_defendant_strategy)
builder.add_node("evidence_attack", run_evidence_attack)
builder.add_node("risk_assessment", run_risk_assessment)
builder.add_node("settlement", run_settlement)

# =====================================================
# LAYER 3: COORDINATION & JUDGMENT
# =====================================================
builder.add_node("strategy_judge", run_strategy_judge)
builder.add_node("recommended_path", run_recommended_path)

# =====================================================
# EDGES: CONNECT LAYERS
# =====================================================

# Layer 1 → Layer 2 (all strategies depend on battlefield understanding)
builder.set_entry_point("battlefield_understanding")
builder.add_edge("battlefield_understanding", "plaintiff_strategy")
builder.add_edge("battlefield_understanding", "defendant_strategy")
builder.add_edge("battlefield_understanding", "evidence_attack")
builder.add_edge("battlefield_understanding", "risk_assessment")
builder.add_edge("battlefield_understanding", "settlement")

# Layer 2 → Layer 3 (all strategies feed into judge)
builder.add_edge("plaintiff_strategy", "strategy_judge")
builder.add_edge("defendant_strategy", "strategy_judge")
builder.add_edge("evidence_attack", "strategy_judge")
builder.add_edge("risk_assessment", "strategy_judge")
builder.add_edge("settlement", "strategy_judge")

# Layer 3 pipeline: judge → recommended_path → END
builder.add_edge("strategy_judge", "recommended_path")
builder.add_edge("recommended_path", END)

graph = builder.compile()