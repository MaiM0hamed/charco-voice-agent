Charco Chicken Voice Agent (Syrian Arabic)

👋 A real-time AI voice assistant that handles phone orders in Syrian Arabic for Charco Chicken. Built using Twilio SIP, PlayHT TTS, Whisper STT, and Streamlit for testing.

📂 Project Structure

charco-voice-agent/
├── api_submit_order.py         # ✅ Order API: /submit-order
├── sip_configtwilio_config.py  # ✅ Twilio SIP voice entry + gather
├── twilio_config.py            # (duplicate SIP logic)
├── stt_ttstts.py               # ⚠️ Using unofficial PlayHT SDK (replace with REST)
├── text_t0speech.py            # ⚠️ Same as above
├── nlp_intent_detector.py      # ✅ Simple Arabic intent detection
├── ui.py                       # ✅ Streamlit testing interface
├── ngrok.exe                   # ✅ For local-to-public tunneling
├── .env                        # 🔐 (not uploaded) should contain PlayHT + Twilio creds
├── README.md                   # 📃 Project documentation
└── data/
    └── orders.json             # ✅ Saved orders (append-only log)

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

