import os
import requests
from pprint import pprint
from dotenv import load_dotenv

# Загрузим переменные из .env
load_dotenv()

class DtApi:
    def __init__(self, base_url: str = "https://distanceandtime.searates.com/v3/api"):
        self.api_key = os.getenv("MY_API_KEY")  # Загружаем ключ из .env или GitHub Secrets
        if not self.api_key:
            raise ValueError("API key not found. Please set MY_API_KEY in .env or GitHub  secrets.")
        self.base_url = base_url

    def get_distance(self, from_city: str, to_city: str, transport_mode: str):
        params = {
            "api_key": self.api_key,
            "from": from_city,
            "to": to_city,
            "transport_modes": transport_mode,
            "alternative_routes": "false",
            "routing_mode": "short"
        }

        headers = {
            "Accept": "application/json"
        }

        response = requests.get(self.base_url, params=params, headers=headers)
        return response
