import os
import requests
import json

class BaseApi:
    def print_response(self, response):
        try:
            data = response.json()
            print(json.dumps(data, indent=2, ensure_ascii=False))
        except ValueError:
            print("Ответ не является JSON:")
            print(response.text)

    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("MY_API_KEY")

    def get_platform_token(self, user_id: int = 24006) -> str:
        url = "https://www.searates.com/auth/platform-token"
        params = {
            "id": user_id,
            "api_key": self.api_key
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        token = data.get("s-token")
        return token


