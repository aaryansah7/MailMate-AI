
# MailMate AI 📧

**An LLM-powered autonomous email assistant built using Python, Ollama, and Gmail SMTP.**

MailMate AI is an intelligent email automation agent that understands natural-language instructions, identifies user intent, retrieves verified contact information, generates personalized email drafts, and sends emails after explicit user confirmation.

## 🚀 Features

- **Natural Language Understanding:** Uses Llama 3.2 (3B) to understand email instructions.
- **Contact Lookup:** Retrieves recipient email addresses from a local JSON database.
- **AI Email Generation:** Automatically generates professional email subjects and bodies.
- **Gmail Integration:** Sends emails using Gmail SMTP and Google App Passwords.
- **Confirmation Guardrail:** Requires explicit user approval before sending emails.
- **Persistent Memory:** Stores previous email interactions using JSON.
- **Contextual Follow-ups:** Reuses previous email content for follow-up instructions.
- **Secure Configuration:** Uses environment variables to protect Gmail credentials.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Core programming language |
| Llama 3.2 (3B) | Language model |
| Ollama | Local LLM inference |
| Requests | Ollama REST API communication |
| Gmail SMTP | Email delivery |
| JSON | Contacts and persistent memory |
| python-dotenv | Environment variable management |

## 🏗️ Project Structure

```text
MailMate-AI/
│
├── agent.py
├── intent_parser.py
├── contact_manager.py
├── email_drafter.py
├── email_sender.py
├── memory_manager.py
├── test_llm.py
│
├── contacts.example.json
├── .gitignore
├── README.md
└── .env.example
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd MailMate-AI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install requests python-dotenv
```

### 4. Install Ollama

Download Ollama from:

https://ollama.com/

Pull the required model:

```bash
ollama pull llama3.2:3b
```

### 5. Configure Gmail credentials

Create a `.env` file in the project directory:

```env
GMAIL_ADDRESS=your_gmail@gmail.com
GMAIL_APP_PASSWORD=your_google_app_password
```

Generate a Google App Password through your Google Account security settings.

Never share or upload your App Password.

### 6. Configure contacts

Copy `contacts.example.json` to `contacts.json` and add your verified contacts.

### 7. Run the application

```bash
python agent.py
```

## 🔄 Agent Workflow

1. User provides a natural-language email instruction.
2. LLM interprets the request and extracts relevant information.
3. Agent retrieves previous context from persistent memory.
4. Contact manager verifies the recipient's email address.
5. LLM generates the email subject and body.
6. Agent displays the email preview.
7. User explicitly confirms or cancels the operation.
8. Gmail SMTP sends the approved email.
9. Interaction details are saved in persistent memory.

## 🔐 Safety Mechanisms

- Unknown contacts are rejected instead of generating guessed email addresses.
- Emails cannot be sent without explicit confirmation.
- Gmail credentials are stored in environment variables.
- Personal contact and memory files are excluded from version control.

## 🧪 Demonstration

Successfully tested:
- Natural-language instruction processing.
- Verified contact retrieval.
- AI-generated email drafting.
- Unknown contact rejection.
- Email cancellation and confirmation.
- Persistent memory and follow-up instructions.
- Actual Gmail SMTP email delivery.

## 👨‍💻 Author

**Aaryan Sah**

B.Tech – Computer Science (AI & ML)

Atlas SkillTech University

---

*MailMate AI — Turning natural-language instructions into actionable email automation.*
