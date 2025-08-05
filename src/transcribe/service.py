import os
os.environ["XDG_CACHE_HOME"] = "/tmp"

import whisper
from src.transcribe.utils import download_temp_audio
from transformers import pipeline

SUPPORTED_LANGUAGES = {
    "vi": "Vietnamese",
    "ja": "Japanese",
    "ko": "Korean",
    "zh-CN": "Chinese",
    "en": "English"
}

model = whisper.load_model("tiny")

def translate_text(text: str, src_lang: str, tgt_lang: str) -> str:
    model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
    translator = pipeline("translation", model=model_name)
    return translator(text, max_length=400)[0]["translation_text"]

def transcribe_from_url(audio_url: str, target_lang: str = "auto") -> str:
    temp_path = download_temp_audio(audio_url)

    try:
        # Step 1: Transcribe audio
        result = model.transcribe(temp_path, language=None if target_lang == "auto" else target_lang)
        original_text = result["text"]
        detected_lang = result["language"]

        # Step 2: Translate if necessary
        if target_lang == "auto" or target_lang == detected_lang:
            print(f"Detected language: {detected_lang}")
            return original_text
        else:
            print(f"Translating from {detected_lang} to {target_lang}")
            return translate_text(original_text, src_lang=detected_lang, tgt_lang=target_lang)
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
