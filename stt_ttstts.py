from playht import PlayHT
from dotenv import load_dotenv
import os

load_dotenv()
playht = PlayHT(
    api_key=os.getenv("PLAYHT_API_KEY"),
    user_id=os.getenv("PLAYHT_USER_ID")
)

def generate_speech(text, output_file):
    try:
        audio = playht.generate(
            text=text,
            voice="ar-SY-Walid-Male"  # Syrian Arabic voice (check PlayHT for exact ID)
        )
        with open(output_file, "wb") as f:
            f.write(audio)
        return True
    except Exception as e:
        print(f"Error in TTS: {str(e)}")
        return False