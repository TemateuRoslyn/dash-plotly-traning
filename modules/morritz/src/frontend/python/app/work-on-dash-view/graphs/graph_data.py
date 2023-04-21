import pandas as pd
import requests

# fonctions permettant de charger les donnees depuis le backend
def load_data():
    datas = requests.get("http://127.0.0.1:8000/accelerometre1/next")
    if datas.status_code == requests.codes.ok:
        json_datas = datas.json()
        df = pd.DataFrame(data=json_datas)
        return df
    else:
        raise Exception