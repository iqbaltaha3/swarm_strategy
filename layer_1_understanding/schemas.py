from pydantic import BaseModel, Field


class BattlefieldAnalysis(BaseModel):
    case_summary: str = Field(default="Case under analysis")
    key_facts: list[str] = Field(default_factory=list)
    legal_issues: list[str] = Field(default_factory=list)
    strength_level: str = Field(default="moderate")  # weak, moderate, strong


class Layer1State(BaseModel):
    complaint: str
    battlefield_analysis: BattlefieldAnalysis
