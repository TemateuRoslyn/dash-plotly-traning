# models/accelerometre1.py

import redis,json,random

list = [94016, 80014, 60659, 10011]

redis_cli = redis.Redis(host='172.17.0.2',port=6379)


class Accelerometre1:
    def __init__(self):
        self.postal_codes = 0
        self.temperature = 0
        self.time = 0

    def to_json(self):
        return json.dumps({
            'time':self.time,
            'temperature':self.temperature,
            'postal_code':self.postal_codes,
            })

    def set_next(self):
        self.time += 1
        self.postal_codes = list[random.randint(0,(len(list)-1))]
        self.temperature = random.uniform(-5,100)
        return redis_cli.set(self.time,self.to_json())

    def get_next(self):
        # self.temperature = self.temperature + [random.uniform(-5,100)]
        # self.time = self.time + [len(self.time)+1]
        # self.postal_codes = self.postal_codes + [list[random.randint(0,(len(list)-1))]]
        return {"temperature": self.temperature, "time": self.time, "code":self.postal_codes}
