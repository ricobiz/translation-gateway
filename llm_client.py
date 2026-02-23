import os
import requests

def translate(text, target_lang):
    api_key = os.getenv('OPENROUTER_API_KEY')
    url = 'https://openrouter.ai/api/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    payload = {
        'model': 'openai/gpt-4o-mini',
        'messages': [
            {'role': 'system', 'content': 'You are a multilingual translator - detect real language even in Latin script, normalize, translate to ' + target_lang + ', return ONLY JSON {detected_lang,normalized_text,translated_text}'},
            {'role': 'user', 'content': text}
        ]
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()