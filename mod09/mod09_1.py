"""
Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin. Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.
"""


class Auto:
    def __init__(self, rekisteri, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

auto = Auto("ABC-123", 142 , 0, 0)

print(f"{auto.rekisteri}, {auto.huippunopeus}, {auto.tämänhetkinen_nopeus}, {auto.kuljettu_matka}")

    
