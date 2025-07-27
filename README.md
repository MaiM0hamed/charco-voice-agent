Charco Chicken Voice Agent (Syrian Arabic)

👋 A real-time AI voice assistant that handles phone orders in Syrian Arabic for Charco Chicken. Built using Twilio SIP, PlayHT TTS, Whisper STT, and Streamlit for testing.

<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/9ef9038b-5a99-443c-ba1d-beeafcf2f5bc" />


🔗 Tool Choices

Feature

Tool/Service

SIP Telephony

Twilio SIP

STT

Whisper / Google STT

TTS

PlayHT (Syrian voices)

Intent NLP

spaCy (ar_core_news_sm)

API

Flask

UI

Streamlit

Deployment

ngrok (local tunnel)

🧪 Testing the UI

To test audio/text flows:

streamlit run ui.py

The UI allows you to:

Upload Syrian Arabic audio

Or type text in Arabic

The agent will:

Transcribe audio (STT)

Detect intent

Generate a response (TTS)

Play the response as audio

🧹 Scenario Guide

📞 Voice Call Flow

Endpoint: POST /voice via Twilio SIP webhook

Handles voice input and triggers /process-speech

📅 Order Request API

Endpoint: POST /submit-order

Example request body:

{
  "name": "Ahmad",
  "order_list": ["Shawarma", "Pepsi"]
}

Example response:

{
  "order_id": "ORD123456",
  "eta": "30 minutes"
}

