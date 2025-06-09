from dotenv import load_dotenv
import os
import requests
import json

from api.base_api import BaseApi

load_dotenv()


class CTApi(BaseApi):
    def __init__(self, api_key=None, base_url="https://tracking.searates.com"):
        self.api_key = api_key or os.getenv("MY_API_KEY")
        self.base_url = base_url.rstrip("/")

    def get_tracking_by_any_number(self, number: str, type: str, force_update: bool, route: bool, ais: bool):

        endpoint = "tracking"
        url = f"{self.base_url}/{endpoint}"

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
        response = requests.get(url, params=params, headers=headers)
        self.print_response(response)
        return response

    def get_route_information_by_any_number(self, number: str, type: str, sealine: str):
        endpoint = "route"
        url = f"{self.base_url}/{endpoint}"
        params = {
            "api_key": self.api_key,
            "number": number,
            "type": type,
            "sealine": sealine,
        }
        headers = {
            "Accept": "application/json"
        }
        response = requests.get(url, params=params, headers=headers)
        self.print_response(response)
        return response

    def get_shipping_line_info(self):
        endpoint = "info/sealines"
        url = f"{self.base_url}/{endpoint}"
        params = {
            "api_key": self.api_key
        }
        headers = {
            "Accept": "application/json"
        }
        response = requests.get(url, params=params, headers=headers)
        self.print_response(response)
        return response

    def get_historical_data(self, number: str, type: str, sealine: str):
        endpoint = "history"
        url = f"{self.base_url}/{endpoint}"
        params = {
            "api_key": self.api_key,
            "number": number,
            "type": type,
            "sealine": sealine
        }
        headers = {
            "Accept": "application/json"
        }
        response = requests.get(url, params=params, headers=headers)
        self.print_response(response)
        return response

    def get_historical_data_id(self, id: int,  number: str, type: str, sealine: str):
        endpoint = "history?id={id}"
        url = f"{self.base_url}/{endpoint}"
        params = {
            "api_key": self.api_key,
            "id": id,
            "number": number,
            "type": type,
            "sealine": sealine
        }
        headers = {
            "Accept": "application/json"
        }
        response = requests.get(url, params=params, headers=headers)
        self.print_response(response)
        return response

