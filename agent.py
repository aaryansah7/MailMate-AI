
from intent_parser import understand_instruction
from contact_manager import find_contact
from email_drafter import generate_email
from email_sender import send_email
from memory_manager import get_last_email, save_memory


def run_agent():

    print("\n================================")
    print("       MAILMATE AI AGENT")
    print("================================")

    print("\nHello! How can I help you today?")

    user_input = input("\nYou: ").strip()

    if not user_input:
        print("[AGENT] Please enter an instruction.")
        return

    # STEP 1: Retrieve previous memory
    previous_email = get_last_email()

    print("\n[AGENT] Retrieving previous context...")

    # STEP 2: Understand user instruction
    print("[AGENT] Analyzing your instruction...")

    try:
        intent = understand_instruction(
            user_input,
            previous_email
        )
    except Exception as error:
        print("[ERROR] Could not understand instruction:", error)
        return

    action = intent.get("action")
    recipient_name = intent.get("recipient_name")

    if action not in ["send_email", "draft_email"]:
        print("[AGENT] Unknown request. Please try again.")
        return

    if not recipient_name:
        print("[AGENT] Please specify the recipient.")
        return

    # STEP 3: Check whether previous email should be reused
    reuse_previous = (
        intent.get("reuse_previous_email", False)
        and previous_email is not None
    )

    if reuse_previous:

        print("[AGENT] Reusing previous email context...")

        purpose = previous_email["purpose"]
        tone = previous_email["tone"]
        subject = previous_email["subject"]
        body = previous_email["body"]

        # Personalize greeting for the new recipient
        old_name = previous_email["recipient_name"]

        old_greeting = f"Dear {old_name},"
        new_greeting = f"Dear {recipient_name},"

        body = body.replace(old_greeting, new_greeting)

    else:

        purpose = intent.get("purpose")
        tone = intent.get("tone", "professional")

        print("[AGENT] Generating a new email...")

        try:
            draft = generate_email(intent, recipient_name)
        except Exception as error:
            print("[ERROR] Email generation failed:", error)
            return

        subject = draft["subject"]
        body = draft["body"]

    # Personalize sender signature
    body = body.replace("[Your Name]", "Aaryan")

    # STEP 4: Look up verified recipient
    print(f"\n[AGENT] Searching contacts for {recipient_name}...")

    contact = find_contact(recipient_name)

    if not contact:

        print("\n[AGENT] Contact not found!")
        print("[AGENT] I will not invent an email address.")
        print("[AGENT] Add a verified address to contacts.json.")
        return

    recipient_email = contact["email"]

    print("[AGENT] Recipient verified successfully!")

    # STEP 5: Display email preview
    print("\n========== EMAIL DRAFT ==========")
    print("To:", recipient_name)
    print("Email:", recipient_email)
    print("Subject:", subject)
    print("\nBody:\n", body)
    print("=================================")

    # STEP 6: Handle draft-only requests
    if action == "draft_email":

        print("\n[AGENT] Draft created. No email was sent.")

        email_data = {
            "recipient_name": recipient_name,
            "recipient_email": recipient_email,
            "subject": subject,
            "body": body,
            "purpose": purpose,
            "tone": tone,
            "status": "drafted"
        }

        save_memory(email_data)

        print("[MEMORY] Draft saved successfully.")
        return

    # STEP 7: Send email with confirmation
    print("\n[AGENT] Your approval is required to send this email.")

    success = send_email(
        recipient_email,
        subject,
        body
    )

    # STEP 8: Update memory only after successful sending
    if success:

        email_data = {
            "recipient_name": recipient_name,
            "recipient_email": recipient_email,
            "subject": subject,
            "body": body,
            "purpose": purpose,
            "tone": tone,
            "status": "sent"
        }

        save_memory(email_data)

        print("\n[MEMORY] Successful interaction saved.")
        print("[AGENT] Task completed successfully!")

    else:

        print("\n[AGENT] Email was not sent.")
        print("[MEMORY] Previous successful memory preserved.")


if __name__ == "__main__":
    run_agent()
