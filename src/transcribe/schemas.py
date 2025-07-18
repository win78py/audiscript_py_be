from pydantic import BaseModel, HttpUrl

class TranscribeRequest(BaseModel):
    url: HttpUrl

class TranscribeResponse(BaseModel):
    text: str
