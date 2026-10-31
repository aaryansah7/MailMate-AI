import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_llm(prompt):
    payload = {
        "model": "llama3.2:3b",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    result = response.json()
    return result["response"]


# Test our LLM connection
if __name__ == "__main__":
    prompt = "You are an AI email assistant. Introduce yourself in 3 sentences."

    answer = ask_llm(prompt)

    print("\n===== MAILMATE AI =====")
    print(answer)
