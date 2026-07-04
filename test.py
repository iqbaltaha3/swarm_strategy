from graph import graph

complaint = """
Rahul borrowed Rs 5 lakh from Amit.

He promised to repay within 3 months.

Despite repeated requests,
he has not repaid.
"""

research_output = {
    "issues": [
        "loan default",
        "possible fraud"
    ],
    "statutes": [
        "Indian Contract Act",
        "BNS cheating provisions"
    ],
    "weaknesses": [
        "No written agreement"
    ]
}

result = graph.invoke(
    {
        "complaint": complaint,
        "research_output": research_output,
    }
)

print("\n===== STRATEGY REPORT =====\n")

print(
    "Win Probability:",
    result["win_probability"]
)

print(
    "\nStrongest Argument:"
)
print(
    result["strongest_argument"]
)

print(
    "\nWeakest Argument:"
)
print(
    result["weakest_argument"]
)

print(
    "\nReasoning:"
)
print(
    result["reasoning"]
)

print(
    "\nRecommended Path:"
)
print(
    result["recommended_path"]
)