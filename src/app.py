from fastapi import FastAPI
from src.transcribe.router import router as transcribe_router

app = FastAPI(title="Audio Transcriber API")

@app.get("/")
async def root():
    return {"status": "ok", "message": "Audio Transcriber is running"}

app.include_router(transcribe_router, prefix="/transcribe")