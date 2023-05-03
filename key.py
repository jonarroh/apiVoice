import os
from dotenv import load_dotenv
from elevenlabs import set_api_key
load_dotenv()

API_KEY = os.getenv("API_KEY")
""" API_KEY is the key to access the Elevenlabs API."""
set_api_key(API_KEY)

from elevenlabs import generate, play, set_api_key

audio = generate(
    text="Hi",
    voice="Bella"
)
print(type(audio))
play(audio)

