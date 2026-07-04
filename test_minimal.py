"""
Minimal 3-Layer Legal Strategy Swarm

Layer 1: Battlefield Understanding
├─ Analyzes case fundamentals
└─ Outputs: case summary, key facts, legal issues, strength level

Layer 2: Specialized Strategies (Parallel)
├─ Plaintiff Strategy Agent
├─ Defendant Strategy Agent
├─ Evidence Attack Agent
├─ Risk Assessment Agent
└─ Settlement Agent
└─ Outputs: specific strategies from each perspective

Layer 3: Coordination & Judgment
├─ Strategy Judge Agent
│  └─ Synthesizes all layer 2 outputs and recommends approach
├─ Win Probability Agent
│  └─ Calculates realistic outcome probabilities
└─ Recommended Path Agent
   └─ Suggests concrete next steps and milestones
"""

from graph import graph
from core.state import StrategyState

# Example usage:
if __name__ == "__main__":
    complaint = """
    Client paid 50% for services on Jan 1, 2024. 
    Services were due by April 1, 2024.
    Defendant did not deliver. 
    No response to communications.
    """
    
    initial_state: StrategyState = {
        "complaint": complaint,
    }
    
    # Run the full 3-layer analysis
    result = graph.invoke(initial_state)
    
    print("=" * 60)
    print("BATTLE FIELD ANALYSIS (Layer 1)")
    print("=" * 60)
    print(result.get("battlefield_analysis"))
    
    print("\n" + "=" * 60)
    print("STRATEGY JUDGMENT (Layer 3)")
    print("=" * 60)
    judgment = result.get("strategy_judgment")
    print(f"Strategy: {judgment.recommended_strategy}")
    print(f"Confidence: {judgment.confidence_level}%")
    print(f"Plaintiff Win Chance: {judgment.plaintiff_win_chance}%")
    print(f"Defendant Win Chance: {judgment.defendant_win_chance}%")
    print(f"Settlement Probability: {judgment.settlement_probability}%")
    print(f"Rationale: {judgment.rationale}")
    
    print("\n" + "=" * 60)
    print("RECOMMENDED PATH (Layer 3)")
    print("=" * 60)
    print(result.get("recommended_path"))
