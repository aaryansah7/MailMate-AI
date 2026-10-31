import json
import os
from datetime import datetime

MEMORY_FILE = "memory.json"


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return {"last_email": None, "history": []}

    with open(MEMORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_memory(email_data):

    memory = load_memory()

    memory["last_email"] = {
        "recipient_name": email_data["recipient_name"],
        "recipient_email": email_data["recipient_email"],
        "subject": email_data["subject"],
        "body": email_data["body"],
        "purpose": email_data["purpose"],
        "tone": email_data["tone"]
    }

    memory["history"].append({
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "recipient": email_data["recipient_name"],
        "subject": email_data["subject"],
        "status": email_data.get("status", "drafted")
    })

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4)


def get_last_email():

    memory = load_memory()

    return memory.get("last_email")


if __name__ == "__main__":

    print("===== MAILMATE AI: MEMORY TEST =====")

    test_email = {
        "recipient_name": "Dr. Kunal Meher",
        "recipient_email": "kunal.meher@atlasuniversity.edu.in",
        "subject": "Thank You for Teaching AI",
        "body": "Dear Dr. Meher,\n\nThank you for teaching us AI.\n\nBest regards,\nAaryan",
        "purpose": "Thank the professor for teaching AI",
        "tone": "professional",
        "status": "drafted"
    }

    save_memory(test_email)

    print("\n[MEMORY] Email details saved successfully!")

    previous_email = get_last_email()

    print("\n[MEMORY] Retrieved previous email:")
    print(json.dumps(previous_email, indent=4))
