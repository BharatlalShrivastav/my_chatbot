from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Predefined chatbot responses
responses = {
    "hi": "Hello! How can I assist you?",
    "how are you": "I'm a chatbot, here to help!",
    "bye": "Goodbye! Have a great day!"
}

@app.route("/", methods=["GET"])  # Add a root route to prevent 404 errors
def home():
    return "Chatbot API is running! Use /chat endpoint to talk to the bot."

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()
    response_text = responses.get(user_message, "Sorry, I don't understand.")
    return jsonify({"response": response_text})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Get the PORT from Render
    app.run(host="0.0.0.0", port=port, debug=True)
