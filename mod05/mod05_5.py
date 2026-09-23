"""
Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen. Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa. Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).
"""

yritykset = 0

while yritykset < 5:
    käyttäjätunnus = input("Mikä on käyttäjätunnuksesi? ")
    salasana = input("Mikä on salasanasi? ")
    if käyttäjätunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break
    elif yritykset == 4:
        print("Pääsy evätty")
    yritykset = yritykset + 1
    