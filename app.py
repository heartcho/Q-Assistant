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

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access and want better responses
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
