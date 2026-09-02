Leiviskä = input("Anna leivisköjen määrä: ")
Naula = input("Anna naulojen määrä: ")
Luoti = input("Anna luotien määrä: ")

Luoti = int(Luoti) * 13.3
print(Luoti)

Naula = int(Naula) * (32 * 13.3)
print(Naula)
Leiviskä = int(Leiviskä) * (20 * (32 * 13.3))
print(Leiviskä)

Massa_yhteensä = Leiviskä + Naula + Luoti

Kg = Massa_yhteensä // 1000
G = Massa_yhteensä % 1000
print(f"Massa nykymittojen mukaan: {Kg:.0f} kilogrammaa ja {G:.2f} grammaa")