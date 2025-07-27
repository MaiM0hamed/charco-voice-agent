from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    response = VoiceResponse()
    response.say("Welcome to Charco Chicken! Please place your order.", voice="Polly.Aditi")
    response.gather(input="speech", action="/process-speech", method="POST")
    return str(response)

@app.route("/process-speech", methods=["POST"])
def process_speech():
    response = VoiceResponse()
    speech_result = request.form.get("SpeechResult", "")
    response.say(f"You said: {speech_result}. Processing your order.", voice="Polly.Aditi")
    return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)