from dotenv import load_dotenv
import os
import requests
import json

from api.base_api import BaseApi

load_dotenv()


class ParcelApi(BaseApi):
    def __init__(self, api_key=None, base_url="https://tracking.searates.com"):
        self.api_key = api_key or os.getenv("MY_API_KEY")
        self.base_url = base_url.rstrip("/")

    def get_parcel_info(self, number: str, carrier_code: str, path: bool ):

        endpoint = "parcel"
        url = f"{self.base_url}/{endpoint}"

        params = {
            "api_key": self.api_key,
            "number": number,
            "carrier_code": carrier_code,
            "path": path,
        }
        headers = {
            "Accept": "application/json"
        }
        response = requests.get(url, params=params, headers=headers)
        self.print_response(response)
        return response


    def get_parcel_companie_info(self ):

        endpoint = "info/parcel_companies"
        url = f"{self.base_url}/{endpoint}"

        params = {
        }
        headers = {
            "Accept": "application/json"
        }
        response = requests.get(url, params=params, headers=headers)
        self.print_response(response)
        return response

