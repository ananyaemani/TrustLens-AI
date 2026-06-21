SCAM_WORDS = [
    "otp",
    "bank account",
    "crypto",
    "send money",
    "registration fee"
]

GROOMING_WORDS = [
    "don't tell your parents",
    "our secret",
    "private photo"
]

MANIPULATION_WORDS = [
    "if you love me",
    "prove it",
    "you don't care"
]

CYBERBULLYING_WORDS = [
    "everyone hates you",
    "nobody likes you",
    "worthless"
]


def calculate_risk(text):

    text = text.lower()

    score = 0
    risks = []

    for word in SCAM_WORDS:
        if word in text:
            score += 3
            risks.append("Scam")

    for word in GROOMING_WORDS:
        if word in text:
            score += 4
            risks.append("Grooming")

    for word in MANIPULATION_WORDS:
        if word in text:
            score += 2
            risks.append("Manipulation")

    for word in CYBERBULLYING_WORDS:
        if word in text:
            score += 3
            risks.append("Cyberbullying")

    return min(score, 10), list(set(risks))