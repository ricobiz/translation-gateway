from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class TranslateRequest(BaseModel):
    text: str
    target_lang: str

class WebhookRequest(BaseModel):
    message: dict

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/translate")
async def translate(request: TranslateRequest):
    # Assuming llm_client is defined and imported
    detected_lang, normalized_text, translated_text = llm_client.translate(request.text, request.target_lang)
    return {
        "detected_lang": detected_lang,
        "normalized_text": normalized_text,
        "translated_text": translated_text
    }

@app.post("/tg/webhook")
async def tg_webhook(request: WebhookRequest):
    message = request.message
    if 'text' in message:
        chat_id = message['chat']['id']
        text = message['text']
        # Call translate with target_lang='Russian'
        result = await translate(TranslateRequest(text=text, target_lang='Russian'))
        # Assuming telegram_client is defined and imported
        telegram_client.send_message(chat_id, result['translated_text'])
    return {"status": "ignored"}