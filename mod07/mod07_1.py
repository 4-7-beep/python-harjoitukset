"""
Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
"""

import random

def heitä_noppa():
    return random.randint(1,6)

silmäluku = 0
while silmäluku != 6:
    silmäluku = heitä_noppa()
    print(silmäluku)

