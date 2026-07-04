JUDGE_SYSTEM = """You are a strategy judge synthesizing all layer 2 analyses.
Make a clear recommendation and assess win probabilities."""

JUDGE_USER = """Analyze all strategies:
- Plaintiff: {plaintiff}
- Defendant: {defendant}
- Evidence: {evidence}
- Risk: {risk}
- Settlement: {settlement}

Provide:
1. Best strategy recommendation (plaintiff_lean, defendant_lean, or settlement_focus)
2. Confidence level (0-100)
3. Win probabilities for plaintiff and defendant (0-100)
4. Settlement probability (0-100)
5. Key factors driving the assessment
6. Detailed rationale
"""

PATH_SYSTEM = """You are a strategic planner.
Recommend concrete next steps and milestones."""

PATH_USER = """Based on case analysis and strategy judgment:
- Battlefield: {battlefield}
- Strategy Judge: {judge}

Recommend:
1. Immediate action
2. Short-term strategy (next 30 days)
3. Long-term strategy (next 6 months)
4. Success metrics to track
"""
