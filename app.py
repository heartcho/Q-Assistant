from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from openai import OpenAI

app = Flask(__name__)
CORS(app, origins=["https://heartcho.github.io"])  # allow your frontend origin

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

client = OpenAI()

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    question = data.get("question", "")
    highlights = data.get("highlights", "")
    teammate = data.get("teammate", "")

    prompt = f"Question: {question}\nTeammate: {teammate}\nHighlights: {highlights}\n\nGenerate a helpful, natural language response:"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )

    answer = response.choices[0].message.content.strip()
    return jsonify({"response": answer})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
