"""
Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys
"""

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, numero):
        while self.nykyinen_kerros < numero:
            self.kerros_ylös()
        while self.nykyinen_kerros > numero:
            self.kerros_alas()

    def kerros_ylös(self):
        self.nykyinen_kerros += 1
        if self.nykyinen_kerros == self.ylin_kerros:
            self.nykyinen_kerros = self.ylin_kerros
        print(f"Nykyinen kerros: {self.nykyinen_kerros}")

    def kerros_alas(self):
        self.nykyinen_kerros -= 1
        if self.nykyinen_kerros == self.alin_kerros:
            self.nykyinen_kerros = self.alin_kerros
        print(f"Nykyinen kerros: {self.nykyinen_kerros}")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissi_lukumäärä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros)
                for _ in range(hissi_lukumäärä)]
    def palohälytys(self):
        for hissi in self.hissit:
            while hissi.nykyinen_kerros > self.alin_kerros:
                hissi.kerros_alas()

    def aja_hissiä(self, hissin_numero, kohdekerros):
        hissi = self.hissit[hissin_numero - 1]
        while hissi.nykyinen_kerros < kohdekerros:
            hissi.kerros_ylös()
        while hissi.nykyinen_kerros > kohdekerros:
            hissi.kerros_alas()

talo1 = Talo(1, 5, 3)
talo1.palohälytys()