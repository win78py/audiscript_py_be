from pydantic import BaseModel
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.transcribe.service import transcribe_from_url

class TranscribeRequest(BaseModel):
    file_url: str

router = APIRouter()

@router.post("")
async def transcribe(req: TranscribeRequest):
    try:
        text = transcribe_from_url(req.file_url)
        return JSONResponse({"transcript": text})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)