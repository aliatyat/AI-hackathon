import json
import time
import requests

# CONFIG
API_KEY = "******************"
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama3-70b-8192"
INPUT_FILE = "input_qa.json"
OUTPUT_FILE = "output_qa_expanded.json"

# LOAD ORIGINAL QA DATA
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    qa_data = json.load(f)

output = []

# FUNCTION TO ASK AI FOR 10 VARIATIONS
def generate_variations(question, answer):
    prompt = (
        "Given the following question and answer, generate 10 reworded question-answer pairs. "
        "The meaning must stay the same, but use different wording/phrasing.\n\n"
        f"Question: {question}\n"
        f"Answer: {answer}\n\n"
        "Format like this (exactly):\n"
        "Q: ...\nA: ...\n\n"
        "Repeat 10 times. No JSON, just clean lines."
    )

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    content = response.json()["choices"][0]["message"]["content"]

    # PARSE Q/A LINES
    lines = content.strip().splitlines()
    qa_pairs = []
    question = ""
    answer = ""

    for line in lines:
        line = line.strip()
        if line.lower().startswith("q:"):
            question = line[2:].strip()
        elif line.lower().startswith("a:"):
            answer = line[2:].strip()
            if question and answer:
                qa_pairs.append({
                    "prompt": question,
                    "completion": answer
                })
                question = ""
                answer = ""

    return qa_pairs

# LOOP THROUGH 100 QA PAIRS
for idx, item in enumerate(qa_data):
    print(f"🔥 Processing QA {idx + 1}/{len(qa_data)}")
    try:
        results = generate_variations(item["prompt"], item["completion"])
        output.extend(results)
    except Exception as e:
        print(f"💥 Error on item {idx + 1}: {e}")
    time.sleep(2)  # Respect rate limit

# SAVE TO OUTPUT FILE
try:
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"✅ DONE: Saved {len(output)} QA pairs to {OUTPUT_FILE}")
except Exception as e:
    print(f"❌ FAILED TO SAVE FILE: {e}")
