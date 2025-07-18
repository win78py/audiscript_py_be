from src.transcribe.utils import download_temp_audio
import whisper
import os

def transcribe_from_url(audio_url: str) -> str:
    model = whisper.load_model("small")

    temp_path = download_temp_audio(audio_url)

    try:
        result = model.transcribe(temp_path)
        return result["text"]
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
