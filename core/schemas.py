from pydantic import BaseModel


class StrategyAssessment(BaseModel):
    win_probability: int
    strongest_argument: str
    weakest_argument: str
    reasoning: str
    recommended_path: str