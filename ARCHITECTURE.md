# 3-Layer Legal Strategy Swarm - Architecture

## Structure Overview

```
Layer 1: Battlefield Understanding
    ↓
Layer 2: Specialized Strategies (Parallel)
    ├─ Plaintiff Strategy
    ├─ Defendant Strategy
    ├─ Evidence Attack
    ├─ Risk Assessment
    └─ Settlement
    ↓
Layer 3: Coordination & Judgment
    ├─ Strategy Judge
    ├─ Win Probability
    └─ Recommended Path
```

## Folder Structure

```
swarm_strategy/
├── core/
│   ├── llm.py              # LLM calls (structured & simple)
│   ├── schemas.py          # Core schemas
│   └── state.py            # Global state management
│
├── layer_1_understanding/
│   ├── schemas.py          # BattlefieldAnalysis
│   ├── prompts.py          # System & user prompts
│   └── battlefield_understanding_agent.py
│
├── layer_2_strategy/
│   ├── schemas.py          # PlaintiffStrategy, DefendantStrategy, etc.
│   ├── prompts.py          # All layer 2 prompts
│   ├── plaintiff_strategy_agent.py
│   ├── defendant_strategy_agent.py
│   ├── evidence_attack_agent.py
│   ├── risk_assessment_agent.py
│   ├── settlement_agent.py
│   └── agents/
│
├── layer_3_coordination/
│   ├── schemas.py          # StrategyJudgment, WinProbability, RecommendedPath
│   ├── prompts.py          # All layer 3 prompts
│   └── judge_agent.py      # All 3 layer 3 agents (judge, win_prob, path)
│
├── graph.py                # LangGraph orchestration (all 3 layers)
├── test_minimal.py         # Example usage
└── test.py                 # Existing tests
```

## Data Flow

1. **Layer 1** analyzes case fundamentals
2. **Layer 2** agents run in parallel, each providing specialized analysis
3. **Layer 3** agents synthesize and recommend actions

## State Schema

All results are stored in `StrategyState`:
- `complaint` → `battlefield_analysis`
- `battlefield_analysis` → all layer 2 outputs
- layer 2 outputs → all layer 3 outputs

## To Run

```python
from graph import graph

initial_state = {"complaint": "..."}
result = graph.invoke(initial_state)

# Access results:
# result["battlefield_analysis"]
# result["plaintiff_strategy"]
# result["defendant_strategy"]
# ... etc ...
# result["strategy_judgment"]
# result["win_probability"]
# result["recommended_path"]
```
