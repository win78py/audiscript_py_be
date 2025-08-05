from pydantic import BaseModel
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.transcribe.service import transcribe_from_url

class TranscribeRequest(BaseModel):
    file_url: str
    language: str = "auto"

router = APIRouter()

@router.post("")
async def transcribe(req: TranscribeRequest):
    try:
        text = transcribe_from_url(req.file_url, req.language)
        return JSONResponse({"transcript": text})
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return JSONResponse({"error": str(e)}, status_code=500)