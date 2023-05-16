from redis import Redis
import json


class RedisServices:
    """La classe aui doit gerer la cnnexion et le stockage des donnees dans une BD Redis"""

    def __init__(self) -> None:
        self.r = Redis(host="localhost", port=6379)

    def save_data(self, key, data):
        self.r.set(key, json.dumps(data))

    def get_data(self, key: str):
        response = self.r.get(key)
        return json.loads(response)
