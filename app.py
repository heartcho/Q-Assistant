from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app, origins=["https://heartcho.github.io"])  # Allow your GitHub Pages frontend

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    question = data.get("question", "")
    highlights = data.get("highlights", "")
    teammate = data.get("teammate", "")

    prompt = f"Question: {question}\nTeammate: {teammate}\nHighlights: {highlights}\n\nGenerate a helpful, natural language response:"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return jsonify({"response": response.choices[0].text.strip()})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
