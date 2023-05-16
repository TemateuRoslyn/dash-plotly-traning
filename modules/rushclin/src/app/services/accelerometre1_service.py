from services.APIRequest import APIRequest
from services.redis_service import RedisServices


class Accelerometre1Service:
    def __init__(self):
        self.request = APIRequest()
        self.redis = RedisServices()
        self.get_next()

    def save_on_redis(self, data):
        self.redis.save_data("acc-1", data)
        # print(self.redis.get_data("acc-1"))

    def get_next(self):
        datas = self.request.get("/accelerometre1/next")
        if datas is not None:
            self.save_on_redis(datas)
