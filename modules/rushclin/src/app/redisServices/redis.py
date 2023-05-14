import redis
from datetime import datetime, timedelta
import json

from services.APIRequest import APIRequest

API_URL = 'http://localhost:5000'

r = redis.Redis(host='localhost', port=6379, db=0)


class RedisServices:
    def __init__(self):
        self.request = APIRequest()

    def update_data(self, url: str):
        response = self.request.get(url)
        if (response):
            key = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            r.set(key, json.dumps(response))
        else:
            print("On ne peut pas faire de la sauvegarde dans Redis")
