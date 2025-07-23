from fastapi import FastAPI
from src.transcribe.router import router as transcribe_router

app = FastAPI(title="Audio Transcriber API")

# Mount the transcription route
app.include_router(transcribe_router, prefix="/transcribe")