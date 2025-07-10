from flask import Flask, request, jsonify
from ai_router import handle_prompt

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    prompt = request.json.get("prompt")
    return jsonify({"result": handle_prompt(prompt)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
