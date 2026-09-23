"""
Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm
"""

tuuma = int(input("Anna senttimetreiksi muutettavat tuumat: "))
while tuuma >= 0:
    tuuma = tuuma * 2.54
    print(tuuma)
    tuuma = (int(input("Anna senttimetreiksi muutettavat tuumat: ")))
else:
    print("Toiminta loppui")

