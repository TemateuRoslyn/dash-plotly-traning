# models/accelerometre1.py

import random

class Accelerometre1:
    def __init__(self):
        self.postal_codes = [94016, 80014, 60659, 10011]
        self.temperature = []
        self.date = []
        self.current_temp = 50
        self.max_temp = 100
        self.min_temp = 0
        self.nom_capteur = "Capteur No 1"

    def get_next(self):
        self.temperature = self.temperature + [random.uniform(-5,100)]
        self.date = self.date + [len(self.date)+1]
        return {"temperature": self.temperature, "date": self.date}
