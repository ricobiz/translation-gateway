from pydantic import BaseModel

class TranslateRequest(BaseModel):
    text: str
    target_lang: str

class TranslateResponse(BaseModel):
    detected_lang: str
    normalized_text: str
    translated_text: str