import os
from dotenv import load_dotenv
from openai import OpenAI
import tempfile

load_dotenv(override=True)
openai = OpenAI()

try:
    print("Testing TTS...")
    tts_response = openai.audio.speech.create(model="tts-1", voice="alloy", input="Hello world")
    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts_response.stream_to_file(temp_audio.name)
    print(f"TTS success: {temp_audio.name}")
except Exception as e:
    print(f"TTS Error: {e}")
