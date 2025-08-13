from dotenv import load_dotenv
import os
import requests
import json

from api.base_api import BaseApi

load_dotenv()


class AIApi(BaseApi):
    def __init__(self, ai_id_number=None, api_key=None, base_url="https://ai-api.searates.com", **kwargs):
        self.ai_id_number = ai_id_number or os.getenv("AI_ID_NUMBER")
        self.api_key = api_key or os.getenv("MY_API_KEY")
        self.base_url = base_url.rstrip("/")

    def post_ai_query(self, query: str):
        url = f"{self.base_url}/client/stream"
        payload = {
            "clientId": self.ai_id_number,
            "query": query
        }

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            #"X-API-KEY": self.api_key  # Добавлен API-ключ
        }

        params = {
            "api_key": self.api_key,
        }

        response = requests.post(url, params=params, headers=headers, json=payload)
        self.print_response(response)
        return response