"""
Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa. Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää.
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

auto = Auto("ABC-123", 142 , 0, 0)

print(f"{auto.rekisteri}, {auto.huippunopeus}, {auto.tämänhetkinen_nopeus}, {auto.kuljettu_matka}")

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(auto.tämänhetkinen_nopeus)

auto.hätäjarrutus(200)
print(auto.tämänhetkinen_nopeus)
    