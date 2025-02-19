from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS to fix browser request issues

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Predefined chatbot responses
responses = {
    "hi": "Hello! How can I assist you?",
    "how are you": "I'm a chatbot, here to help!",
    "bye": "Goodbye! Have a great day!",
    "what is your name": "I am your friendly chatbot!",
    "who created you": "I was created by an awesome developer!"
}

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()
    response_text = responses.get(user_message, "Sorry, I don't understand that.")
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True)
