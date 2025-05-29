from dotenv import load_dotenv
import os
import requests

load_dotenv()


class CTApi:
    def __init__(self, api_key=None, base_url="https://tracking.searates.com/tracking"):
        self.api_key = api_key or os.getenv("MY_API_KEY")
        self.base_url = base_url

    def get_tracking_by_any_number(self, number: str, type: str, force_update: bool, route: bool, ais: bool):
        params = {
            "api_key": self.api_key,
            "number": number,
            "type": type,
            "force_update": force_update,
            "route": route,
            "ais": ais
        }
        headers = {
            "Accept": "application/json"
        }

        response = requests.get(self.base_url, params=params, headers=headers)
        return response
