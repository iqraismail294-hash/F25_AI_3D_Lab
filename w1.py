
def scholarship(score, documents, recommendation, attendance):
    if (score >= 70 and documents and recommendation and attendance >= 70):
        return "eligible"
    else:
        return "not eligible"
conditions = [
    {
        "name": "Score failure",
        "score": 65,
        "documents": True,
        "recommendation": True,
        "attendance": 80,
        "expected": "not eligible",
        "reason": "The score is less than 70."
    },
    {
        "name": "Documents failure",
        "score": 80,
        "documents": False,
        "recommendation": True,
        "attendance": 80,
        "expected": "not eligible",
        "reason": "The documents are incomplete."
    },
    {
        "name": "Recommendation failure",
        "score": 80,
        "documents": True,
        "recommendation": False,
        "attendance": 80,
        "expected": "not eligible",
        "reason": "The recommendation letter is missing."
    },
    {
        "name": "All conditions passed",
        "score": 85,
        "documents": True,
        "recommendation": True,
        "attendance": 80,
        "expected": "eligible",
        "reason": "All conditions are satisfied."
    }
]
for condition in conditions:
    real = scholarship(
        condition["score"],
        condition["documents"],
        condition["recommendation"],
        condition["attendance"]
    )
    print("\nCase:", condition["name"])
    print("Input:", {
        "score": condition["score"],
        "documents": condition["documents"],
        "recommendation": condition["recommendation"],
        "attendance": condition["attendance"]
    })
    print("Expected result:", condition["expected"])
    print("Actual result:", real)
    print("Reason:", condition["reason"])
    print("Test passed:", real == condition["expected"])
