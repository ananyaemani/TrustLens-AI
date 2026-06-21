import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.0-flash")

def analyze_with_ai(text):

    prompt = f"""
You are TrustLens AI.

Analyze the following message.

Detect:
- Scam
- Manipulation
- Grooming
- Cyberbullying
- Phishing

Provide:
1. Risk Score (0-10)
2. Threat Level
3. Detected Risks
4. Explanation
5. Safety Advice

Message:
{text}
"""

    response = model.generate_content(prompt)

    return response.text