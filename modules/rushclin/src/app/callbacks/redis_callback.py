from dash import Dash, Input, Output
from redisServices import RedisServices


class RedisCallback:
    def __init__(self, app) -> None:
        self.app = app
        self.redis_service = RedisServices()

    def register(self):
        @self.app.callback(

        )
