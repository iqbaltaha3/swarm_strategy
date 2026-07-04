from pydantic import BaseModel, Field


class PlaintiffStrategy(BaseModel):
    strong_arguments: list[str] = Field(default_factory=list)
    evidence_priorities: list[str] = Field(default_factory=list)
    attack_vectors: list[str] = Field(default_factory=list)


class DefendantStrategy(BaseModel):
    defense_lines: list[str] = Field(default_factory=list)
    vulnerability_areas: list[str] = Field(default_factory=list)
    counter_strategies: list[str] = Field(default_factory=list)


class EvidenceAttack(BaseModel):
    vulnerable_evidence: list[str] = Field(default_factory=list)
    attack_methods: list[str] = Field(default_factory=list)
    counterarguments: list[str] = Field(default_factory=list)


class RiskAnalysis(BaseModel):
    plaintiff_risks: list[str] = Field(default_factory=list)
    defendant_risks: list[str] = Field(default_factory=list)
    critical_issues: list[str] = Field(default_factory=list)


class SettlementFramework(BaseModel):
    settlement_range: str = Field(default="TBD")
    key_concessions: list[str] = Field(default_factory=list)
    deal_breakers: list[str] = Field(default_factory=list)
