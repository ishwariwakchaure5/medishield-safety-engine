from config import client
import time
import openai

SYSTEM_PROMPT = """
You are MediShield AI – a healthcare safety assistant.

RULES:
- Do NOT diagnose or give medication dosages.
- Give only general, educational explanations.
- Encourage professional consultation when appropriate.
"""

# Basic backup answers for safe queries (used when API fails)
FALLBACK_RESPONSES = {
    "blood pressure": "Blood pressure can rise due to stress, lack of exercise, high salt intake, obesity, smoking, alcohol use, genetics, and certain medical conditions like kidney or hormonal disorders.",
    "hypertension": "Hypertension means high blood pressure caused by lifestyle factors, age, genetics, obesity, stress, excess salt, and lack of physical activity."
}

def get_response(prompt):

    for attempt in range(3):
        try:
            completion = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}
                ]
            )
            return completion.choices[0].message.content.strip()

        except Exception:
            print("⏳ Rate limited. Retrying...")
            time.sleep(8)

    # ✅ Offline SAFETY fallback instead of showing an error
    for key in FALLBACK_RESPONSES:
        if key in prompt.lower():
            return FALLBACK_RESPONSES[key]

    return "I’m unable to connect right now. For reliable medical information, please consult a healthcare professional."
