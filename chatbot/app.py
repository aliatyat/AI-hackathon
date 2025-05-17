from flask import Flask, request, jsonify, render_template
import json
from difflib import get_close_matches
import os

app = Flask(__name__, template_folder='../templates')

def load_qa_dataset():
    # Use absolute path to find data.json
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, "data.json")
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)

def find_answer(question, qa_data):
    questions = [item["prompt"] for item in qa_data]
    match = get_close_matches(question, questions, n=1, cutoff=0.6)
    if match:
        for item in qa_data:
            if item["prompt"] == match[0]:
                return item["completion"]
    return "I don't have an answer for that. Try asking about 42Amman or Jordan!"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    
    try:
        qa_data = load_qa_dataset()
        answer = find_answer(question, qa_data)
        return jsonify({"answer": answer})
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"answer": "Sorry, I encountered an error. Please try again later."})

if __name__ == "__main__":
    app.run(debug=True)