
import json

class BaseApi:
    def print_response(self, response):
        try:
            data = response.json()
            print(json.dumps(data, indent=2, ensure_ascii=False))
        except ValueError:
            print("Ответ не является JSON:")
            print(response.text)