from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question")
    return jsonify({"answer": f"Echo: {question}"})

if __name__ == "__main__":
    app.run(debug=True)