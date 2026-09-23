"""
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.
"""
import random

def noppa(tahkot):
    return random.randint(1,maksimi)

silmäluku = 0
maksimi = int(input("Kuinka monta tahkoa nopassa on? "))
while silmäluku != maksimi:
    silmäluku = noppa(maksimi)
    print(silmäluku)

