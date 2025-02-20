import os
import json
import google.cloud.dialogflow_v2 as dialogflow
from google.oauth2 import service_account
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# ✅ Load Google Dialogflow credentials safely
if "GOOGLE_CREDENTIALS" not in os.environ:
    raise ValueError("GOOGLE_CREDENTIALS environment variable not found!")

credentials_info = json.loads(os.environ["GOOGLE_CREDENTIALS"])
credentials = service_account.Credentials.from_service_account_info(credentials_info)

# ✅ Function to get AI response from Dialogflow
def get_ai_response(user_message, session_id="12345"):
    client = dialogflow.SessionsClient(credentials=credentials)
    session = client.session_path("mychatbot-451407", session_id)

    text_input = dialogflow.TextInput(text=user_message, language_code="en")
    query_input = dialogflow.QueryInput(text=text_input)
    response = client.detect_intent(session=session, query_input=query_input)

    return response.query_result.fulfillment_text

@app.route("/", methods=["GET"])
def home():
    return "Chatbot API is running!"

# ✅ Fix /chat to handle both GET & POST correctly
@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "GET":
        user_message = request.args.get("message", "").lower()
    else:
        user_message = request.json.get("message", "").lower()

    response_text = get_ai_response(user_message)
    return jsonify({"response": response_text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use PORT from environment if available
    app.run(host="0.0.0.0", port=port, debug=True)
