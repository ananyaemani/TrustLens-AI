def get_advice(score):

    if score <= 2:
        return "Low Risk. Stay aware."

    elif score <= 5:
        return """
Moderate Risk.

Be cautious.
Avoid sharing personal information.
Verify claims independently.
"""

    else:
        return """
High Risk.

Do not share personal information,
photos, OTPs, or money.

Talk to a trusted adult,
teacher, parent, or guardian.
"""