import requests
from pprint import pprint

class DtApi:
    def __init__(self, base_url: str = "https://distanceandtime.searates.com/v3/api"):
        self.api_key = "K-02CCA95B-6516-4E83-8F63-6748AAF40FB5"
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
