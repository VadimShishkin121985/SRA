from dotenv import load_dotenv
import os
import requests
import json

from api.base_api import BaseApi

load_dotenv()


class ATApi(BaseApi):
    def __init__(self, api_key=None, base_url="https://tracking.searates.com"):
        self.api_key = api_key or os.getenv("MY_API_KEY")
        self.base_url = base_url.rstrip("/")

    def get_air_tracking_awb(self, number: str, path: bool):
        endpoint = "air"
        url = f"{self.base_url}/{endpoint}"

        params = {
            "api_key": self.api_key,
            "number": number,
            "path": path,
        }
        headers = {
            "Accept": "application/json"
        }
        response = requests.get(url, params=params, headers=headers)
        self.print_response(response)
        return response
