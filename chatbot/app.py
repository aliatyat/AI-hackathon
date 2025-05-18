from flask import Flask, request, jsonify, render_template
import json
from difflib import get_close_matches
import os
from similarity import *
from transformers  import AutoTokenizer , AutoModelForCausalLM , pipeline
app = Flask(__name__, template_folder='../templates')

def load_qa_dataset():
    # Use absolute path to find data.json
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, "data.json")
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)

def find_answer(question, qa_data):
    questions = [item["prompt"] for item in qa_data]
    match = get_close_matches(question, questions, n=1, cutoff=0.65)
    if match:
        for item in qa_data:
            if item["prompt"] == match[0]:
                return item["completion"]
    return "I don't have an answer for that. Try asking about 42Amman or Jordan!"

@app.route("/")
def index():
    return render_template("index.html")

# Load model and tokenizer
model_path = "42amman_model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

# Create pipeline
chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

@app.route('/api/chat', methods=['POST'])
def chat(question):
    prompt = f"""\n Q: {question}.\nA:"""
    
    # Generate response
    response = chatbot(
        prompt,
        max_length=150,
        temperature=0.5,
        top_p=0.92,
        no_repeat_ngram_size=2,
        num_return_sequences=1
    )
    
    # Extract answer from response
    generated_text = response[0]['generated_text']
    answer = generated_text.split("A:")[1].strip() if "A:" in generated_text else generated_text
    
    return jsonify({"answer": answer})

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    if not is_similar_question(question,"data.json",0.7 ):#user_question, json_path, threshold=0.8
        return jsonify({"answer": "Please Ask a question about 42Amman or Jordan :)"})
    try:
        qa_data = load_qa_dataset()
        answer = chat(question)
        return answer
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"answer": "Sorry, I encountered an error. Please try again later."})

if __name__ == "__main__":
    app.run(debug=True)