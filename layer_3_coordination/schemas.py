from pydantic import BaseModel, Field


class StrategyJudgment(BaseModel):
    recommended_strategy: str = Field(default="settlement_focus")  # plaintiff_lean, defendant_lean, settlement_focus
    confidence_level: int = Field(default=50, ge=0, le=100)  # 0-100
    plaintiff_win_chance: int = Field(default=50, ge=0, le=100)  # 0-100
    defendant_win_chance: int = Field(default=50, ge=0, le=100)  # 0-100
    settlement_probability: int = Field(default=50, ge=0, le=100)  # 0-100
    key_factors: list[str] = Field(default_factory=list)
    rationale: str = Field(default="Analysis pending")


class RecommendedPath(BaseModel):
    immediate_action: str = Field(default="Assess case strength")
    short_term_strategy: str = Field(default="Gather evidence and documentation")
    long_term_strategy: str = Field(default="Pursue settlement or litigation")
    success_metrics: list[str] = Field(default_factory=list)
