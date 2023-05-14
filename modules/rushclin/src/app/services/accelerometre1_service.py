from services.APIRequest import APIRequest
from redisServices.redis import RedisServices


class Accelerometre1Service:
    def __init__(self):
        self.request = APIRequest()
        self.redis_services = RedisServices()

    def get_next(self):
        self.redis_services.update_data('/accelerometre1/next')
        datas = self.request.get('/accelerometre1/next')
        if datas is not None:
            return datas
        else:
            return None
