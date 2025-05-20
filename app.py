from flask import Flask, request, jsonify, send_from_directory
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Serve your index.html from the "static" folder at root URL
@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

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
    port = int(os.environ.get("PORT", 5000))  # Use Render's assigned port or default to 5000
    app.run(host="0.0.0.0", port=port)
