from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def load_qa_dataset():
    with open("data.json", "r") as f:
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
"""
@app.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question")
    qa_data = load_qa_dataset()
    answer = find_answer(question, qa_data)
    return jsonify({"answer": answer})
"""

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question', '')
    # Your DistilGPT-2 model processing here
    # ...
    return jsonify({'answer': response})


if __name__ == "__main__":
    app.run(debug=True)