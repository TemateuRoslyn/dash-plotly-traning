# models/accelerometre1.py

import random

list = [94016, 80014, 60659, 10011]

class Accelerometre1:
    def __init__(self):
        self.postal_codes = []
        self.temperature = []
        self.date = []
        self.current_temp = 50
        self.max_temp = 100
        self.min_temp = 0
        self.nom_capteur = "Capteur No 1"

    def get_next(self):
        self.temperature = self.temperature + [random.uniform(-5,100)]
        self.date = self.date + [len(self.date)+1]
        self.postal_codes = self.postal_codes + [list[random.randint(0,(len(list)-1))]]
        return {"temperature": self.temperature, "time": self.date, "code":self.postal_codes}
