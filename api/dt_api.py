from dotenv import load_dotenv
import os

load_dotenv()  # Безопасно, даже если .env нет — для локального запуска

class DtApi:
    def __init__(self, api_key=None, base_url="https://distanceandtime.searates.com/v3/api"):
        self.api_key = api_key or os.getenv("MY_API_KEY")
        if not self.api_key:
            raise ValueError("API key is missing. Check .env or environment.")
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
