
import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"


def understand_instruction(user_input, previous_email=None):

    previous_context = (
        json.dumps(previous_email, indent=2)
        if previous_email
        else "No previous email available."
    )

    prompt = f"""
    You are the reasoning engine of MailMate AI,
    an intelligent email assistant.

    Analyze the user's latest instruction.

    Previous email context:
    {previous_context}

    Current user instruction:
    {user_input}

    Return ONLY valid JSON with these fields:

    {{
        "action": "send_email, draft_email, or unknown",
        "recipient_name": "recipient name or null",
        "subject": "email subject or null",
        "purpose": "purpose of the email",
        "tone": "professional, friendly, or formal",
        "is_followup": true,
        "reuse_previous_email": false,
        "missing_information": []
    }}

    Rules:

    1. Understand the current instruction.
    2. If the user says "same email", "send it again",
       or similar, use the previous email context.
    3. Extract a newly specified recipient if provided.
    4. If the user does not specify a new recipient,
       only reuse the previous recipient when the
       instruction clearly refers to that recipient.
    5. Do not invent email addresses.
    6. Do not invent recipient names or facts.
    7. Set is_followup to true for follow-up instructions.
    8. Set reuse_previous_email to true when the user
       wants to reuse the previous email's content.
    9. If there is no previous email, do not pretend
       that previous context exists.
    10. If important information is missing, mention it
        in missing_information.

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

    intent = json.loads(result["response"])

    # Detect explicit requests to reuse previous email
    instruction = user_input.lower()

    reuse_phrases = [
        "same email",
        "same message",
        "send it again",
        "send that email",
        "forward the same"
    ]

    if previous_email and any(
        phrase in instruction for phrase in reuse_phrases
    ):
        intent["is_followup"] = True
        intent["reuse_previous_email"] = True

    return intent



if __name__ == "__main__":

    user_input = input("\nWhat would you like me to do? ")

    intent = understand_instruction(user_input)

    print("\n===== MAILMATE AI: UNDERSTANDING =====")
    print(json.dumps(intent, indent=4))
