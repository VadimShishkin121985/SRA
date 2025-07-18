from dotenv import load_dotenv
import os
import requests
import json

from api.base_api import BaseApi

load_dotenv()


class LEApi(BaseApi):
    def __init__(self, api_key=None, base_url="https://rates.searates.com/graphql"):
        super().__init__(api_key)
        self.base_url = base_url.rstrip("/")

    def get_rates(self, variables: dict) -> requests.Response:

        query = """
            {
              rates(
                includedServices: %(includedServices)s
                portFromFees: %(portFromFees)s
                portToFees: %(portToFees)s
                shippingType: %(shippingType)s
                coordinatesFrom: %(coordinatesFrom)s
                coordinatesTo: %(coordinatesTo)s
                date: "%(date)s"
                container: %(container)s
              ) {
                general {
                  shipmentId
                  validityFrom
                  validityTo
                  individual
                  totalPrice
                  totalCurrency
                  totalTransitTime
                  totalCo2 {
                    amount
                    price
                  }
                  dfaRate
                  alternative
                  expired
                  spaceGuarantee
                  spot
                  indicative
                  rateOwner
                }
                points {
                  id
                  rateId
                  location {
                    id
                    name
                    country
                    lat
                    lng
                    code
                    inaccessible
                    pointType
                  }
                  shippingType
                  provider
                  providerLogo
                  loads {
                    id
                    unit
                    amount
                  }
                  pointTariff {
                    name
                    abbr
                    price
                    currency
                    profileId
                  }
                  routeTariff {
                    name
                    abbr
                    price
                    currency
                  }
                  lumpsumTariff {
                    price
                    currency
                  }
                  co2 {
                    amount
                    price
                    placeAmount
                    placePrice
                  }
                  transitTime {
                    rate
                    port
                    route
                  }
                  distance
                  totalPrice
                  totalCurrency
                  pointTotal
                  routeTotal
                  terms
                }
              }
            }
           """ % {
            "includedServices": variables["includedServices"],
            "portFromFees": str(variables["portFromFees"]).lower(),
            "portToFees": str(variables["portToFees"]).lower(),
            "shippingType": variables["shippingType"],
            "coordinatesFrom": str(variables["coordinatesFrom"]),
            "coordinatesTo": str(variables["coordinatesTo"]),
            "date": variables["date"],
            "container": variables["container"]
        }

        token = self.get_platform_token()

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

        payload = {
            "query": query
        }

        response = requests.post(self.base_url, json=payload, headers=headers)
        self.print_response(response)
        # print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        return response



