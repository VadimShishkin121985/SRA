from dotenv import load_dotenv
import os
import requests
import json

from api.base_api import BaseApi

load_dotenv()


class SSApi(BaseApi):
    def __init__(self, api_key=None, base_url="https://schedules.searates.com/api/v2"):
        self.api_key = api_key or os.getenv("MY_API_KEY")
        self.base_url = base_url.rstrip("/")

    def get_schedules_by_points_general_cargo(self, cargo_type: str, origin: str, destination: str, from_date: str,
                                              weeks: int, sort: str, direct_only: bool, multimodal: bool):
        endpoint = "schedules/by-points"
        url = f"{self.base_url}/{endpoint}"
        headers = {
            "X-API-KEY": self.api_key
        }
        params = {
            "cargo_type": cargo_type,
            "origin": origin,
            "destination": destination,
            "from_date": from_date,
            "weeks": weeks,
            "sort": sort,
            "direct_only": str(direct_only).lower(),
            "multimodal": str(multimodal).lower()
        }
        response = requests.get(url, params=params, headers=headers)
        self.print_response(response)
        return response

    def get_schedules_by_vessel(self, imo: int, ):
        endpoint = "schedules/by-vessel"
        url = f"{self.base_url}/{endpoint}"
        headers = {
            "X-API-KEY": self.api_key
        }
        params = {
            "imo": imo,
        }
        response = requests.get(url, params=params, headers=headers)
        self.print_response(response)
        return response

    def get_schedules_by_ports(self, locode: str, from_date: str, weeks: int ):
        endpoint = "schedules/by-port"
        url = f"{self.base_url}/{endpoint}"
        headers = {
            "X-API-KEY": self.api_key
        }
        params = {
            "locode": locode,
            "from_date": from_date,
            "weeks": weeks
        }
        response = requests.get(url, params=params, headers=headers)
        self.print_response(response)
        return response

    def get_schedules_carriers(self, schedule_type: str, cargo_type: str):
        endpoint = "carriers"
        url = f"{self.base_url}/{endpoint}"
        headers = {
            "X-API-KEY": self.api_key
        }
        params = {
            "schedule_type": schedule_type,
            "cargo_type": cargo_type,
        }
        response = requests.get(url, params=params, headers=headers)
        self.print_response(response)
        return response

    def get_schedules_carrier_entry_scac(self, scac: str):
        endpoint = "carriers"
        url = f"{self.base_url}/{endpoint}/{scac.upper()}"
        headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        self.print_response(response)
        return response

    def get_schedules_carrier_entry_imo(self, imo: int):
        endpoint = "vessels"
        url = f"{self.base_url}/{endpoint}/{imo}"
        headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        self.print_response(response)
        return response

    def get_schedules_port_entry(self, locode: str):
        endpoint = "ports"
        url = f"{self.base_url}/{endpoint}/{locode.upper()}"

        headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response
