import streamlit as st
from stt_tts.stt import transcribe_audio
from nlp.intent_detector import detect_intent
from nlp.dialogue_flow import handle_dialogue
from stt_tts.tts import generate_speech
import os

st.title("Charco Chicken Voice Agent Tester")

# Audio upload
audio_file = st.file_uploader("Upload Syrian Arabic audio", type=["wav", "mp3"])
if audio_file:
    # Save uploaded file
    with open("temp_audio.wav", "wb") as f:
        f.write(audio_file.read())
    transcribed_text = transcribe_audio("temp_audio.wav")
    st.write(f"Transcribed Text: {transcribed_text}")
    intent = detect_intent(transcribed_text)
    st.write(f"Detected Intent: {intent}")
    response = handle_dialogue(intent, transcribed_text)
    st.write(f"Agent Response: {response}")
    if generate_speech(response, "output.mp3"):
        st.audio("output.mp3")

# Text input
text_input = st.text_input("Or type in Syrian Arabic")
if text_input:
    intent = detect_intent(text_input)
    st.write(f"Detected Intent: {intent}")
    response = handle_dialogue(intent, text_input)
    st.write(f"Agent Response: {response}")
    if generate_speech(response, "output.mp3"):
        st.audio("output.mp3")