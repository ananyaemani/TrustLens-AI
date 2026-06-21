SCAM_KEYWORDS = [
    "otp",
    "bank account",
    "crypto",
    "send money"
]

MANIPULATION_KEYWORDS = [
    "if you love me",
    "prove you care"
]

GROOMING_KEYWORDS = [
    "don't tell your parents",
    "send a photo",
    "private picture",
    "our secret"
]

def analyze_text(text):

    text = text.lower()

    risks = []
    score = 0

    for word in SCAM_KEYWORDS:
        if word in text:
            risks.append("Scam")
            score += 3

    for word in MANIPULATION_KEYWORDS:
        if word in text:
            risks.append("Manipulation")
            score += 2

    for word in GROOMING_KEYWORDS:
        if word in text:
            risks.append("Grooming")
            score += 4

    return {
        "risks": list(set(risks)),
        "score": min(score, 10)
    }