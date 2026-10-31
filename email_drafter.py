import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_email(intent, recipient_name):

    prompt = f"""
    You are MailMate AI, a professional email writer.

    Write an email using the following information:

    Recipient: {recipient_name}
    Purpose: {intent.get("purpose")}
    Tone: {intent.get("tone", "professional")}
    Suggested subject: {intent.get("subject")}

    Requirements:
    1. Generate an appropriate subject if none is provided.
    2. Write a clear and professional email body.
    3. Do not invent facts or commitments.
    4. Do not invent meeting details or dates.
    5. Address the recipient appropriately.

    Return ONLY valid JSON in this format:

    {{
        "subject": "Email subject",
        "body": "Complete email body"
    }}
    """

    payload = {
        "model": "llama3.2:3b",
        "prompt": prompt,
        "stream": False,
        "format": "json"
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    result = response.json()

    email = json.loads(result["response"])

    if not email.get("subject") or not email.get("body"):
        raise ValueError("LLM generated an incomplete email.")

    return email


if __name__ == "__main__":

    test_intent = {
        "purpose": "Thank Dr. Meher for teaching us AI",
        "tone": "professional",
        "subject": None
    }

    draft = generate_email(test_intent, "Dr. Kunal Meher")

    print("\n===== GENERATED EMAIL =====")
    print("Subject:", draft["subject"])
    print("\nBody:\n", draft["body"])
