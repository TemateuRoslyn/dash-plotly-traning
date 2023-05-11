from services.APIRequest import APIRequest


class Accelerometre2Service:
    def __init__(self):
        self.request = APIRequest()

    def get_next(self):
        datas = self.request.get('/accelerometre2/next')
        if datas is not None:
            return datas
        else:
            return None
