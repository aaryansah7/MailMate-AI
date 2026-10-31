
import os
import smtplib

from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


def send_email(recipient_email, subject, body):

    if not GMAIL_ADDRESS or not GMAIL_APP_PASSWORD:
        print("[ERROR] Gmail credentials missing.")
        return False

    # Display email preview
    print("\n========== EMAIL PREVIEW ==========")
    print("From:", GMAIL_ADDRESS)
    print("To:", recipient_email)
    print("Subject:", subject)
    print("\nBody:\n", body)
    print("===================================")

    # Safety confirmation
    confirmation = input(
        "\nType SEND to confirm sending this email: "
    )

    if confirmation.strip() != "SEND":
        print("\n[AGENT] Email sending cancelled.")
        return False

    try:
        message = EmailMessage()

        message["From"] = GMAIL_ADDRESS
        message["To"] = recipient_email
        message["Subject"] = subject

        message.set_content(body)

        print("\n[SMTP] Connecting to Gmail...")

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:

            server.starttls()

            server.login(
                GMAIL_ADDRESS,
                GMAIL_APP_PASSWORD
            )

            server.send_message(message)

        print("\n[SUCCESS] Email sent successfully!")

        return True

    except Exception as error:

        print("\n[ERROR] Email could not be sent:", error)

        return False

