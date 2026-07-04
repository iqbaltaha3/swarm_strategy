from typing import TypedDict, Any

class StrategyState(TypedDict, total=False):

    # Input
    complaint: str
    
    # Layer 1: Battlefield Understanding
    battlefield_analysis: Any
    
    # Layer 2: Specialized Strategies
    plaintiff_strategy: Any
    defendant_strategy: Any
    evidence_attack: Any
    risk_analysis: Any
    settlement: Any
    
    # Layer 3: Coordination & Judgment
    strategy_judgment: Any
    win_probability: Any
    recommended_path: Any