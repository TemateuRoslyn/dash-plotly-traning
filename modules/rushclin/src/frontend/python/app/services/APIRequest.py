import requests


class APIRequest:
    def __init__(self, url):
        self.url = url

    def make_request(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
