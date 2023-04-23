from services.APIRequest import APIRequest


class Comparateur1Service:
    def __init__(self):
        self.request = APIRequest()

    def get_next(self):
        datas = self.request.get('/comparateur1/next')
        if datas is not None:
            return datas
        else:
            return None
