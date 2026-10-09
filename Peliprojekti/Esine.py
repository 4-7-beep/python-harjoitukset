class Esine:
    def __init__(self, nimi, hajoamispiste):
        self.nimi = nimi
        self.hajoamispiste = hajoamispiste

import time
import random

askel = random.randint(3,8)

def kävele(askel):
    print("Kävelet", end="", flush=True)
    for i in range(askel):
        time.sleep(0.5)
        if i % 2 == 0:
            print(" \u02D9", end="", flush=True)
        else:
            print(" .", end="", flush=True)
    print()

kävele(askel)