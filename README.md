Charco Chicken Voice Agent (Syrian Arabic)

👋 A real-time AI voice assistant that handles phone orders in Syrian Arabic for Charco Chicken. Built using Twilio SIP, PlayHT TTS, Whisper STT, and Streamlit for testing.

charco-voice-agent/
│
├── api_submit_order.py          # ✅ Order API: /submit-order
├── sip_configtwilio_config.py   # ✅ Twilio SIP voice entry + gather
├── twilio_config.py             # (duplicate SIP logic)
├── stt_ttstts.py                # ⚠️ Using unofficial PlayHT SDK (replace with REST)
├── text_t0speech.py             # ⚠️ Same as above
├── nlp_intent_detector.py       # ✅ Simple Arabic intent detection
├── ui.py                        # ✅ Streamlit testing interface
├── ngrok.exe                    # ✅ For local-to-public tunneling
├── .env                         # 🔐 (not uploaded) should contain PlayHT + Twilio creds
├── README.md                    # 🚧 To be written (see below)
└── data/
    └── orders.json              # ✅ Saved orders (append-only log)


🔗 Tool Choices
Feature	Tool/Service
SIP Telephony	Twilio SIP
STT	Whisper / Google STT
TTS	PlayHT (Syrian voices)
Intent NLP	spaCy (ar_core_news_sm)
API	Flask
UI	Streamlit
Deployment	ngrok (local tunnel)

🧪 Testing UI

To test audio/text flows:
streamlit run ui.py
You can upload Syrian Arabic audio or type input. The agent will:
Transcribe STT
Detect intent
Generate reply using TTS
Play the response audio
🧹 Scenario Guide
Voice Call → via Twilio SIP webhook (/voice)
Order Request → /submit-order with JSON body:
{
  "name": "Ahmad",
  "order_list": ["Shawarma", "Pepsi"]
}
Returns:
{
  "order_id": "ORD123456",
  "eta": "30 minutes"
}
