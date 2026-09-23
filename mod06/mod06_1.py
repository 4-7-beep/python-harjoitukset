"""
Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.
"""

import random

arpakuutio_määrä = int(input("Anna arpakuutioiden määrä: "))
summa = 0

for i in range(arpakuutio_määrä):
    heitto = random.randint(1,6)
    summa += heitto
    
print(summa)

