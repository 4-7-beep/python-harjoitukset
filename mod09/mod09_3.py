"""Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän. Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt. Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.
"""

class Auto:
    def __init__(self, rekisteri, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self,nopeuden_muutos):
        uusi_nopeus = self.tämänhetkinen_nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            uusi_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            uusi_nopeus = 0
        self.tämänhetkinen_nopeus = uusi_nopeus

    def hätäjarrutus(self,nopeuden_muutos):
        uusi_nopeus = self.tämänhetkinen_nopeus - nopeuden_muutos
        if uusi_nopeus < 0:
            uusi_nopeus = 0
        self.tämänhetkinen_nopeus = uusi_nopeus

    def kulje(self,tuntimäärä):
        matkan_muutos = self.tämänhetkinen_nopeus * tuntimäärä
        uusi_kuljettu_matka = self.kuljettu_matka + matkan_muutos
        self.kuljettu_matka = uusi_kuljettu_matka

auto = Auto("ABC-123", 142 , 60, 2000)

print(f"{auto.rekisteri}, {auto.huippunopeus}, {auto.tämänhetkinen_nopeus}, {auto.kuljettu_matka}")


auto.kulje(1.5)
print(auto.kuljettu_matka)