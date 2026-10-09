class Pelaaja:
    def __init__(self, nimi, ikä):
        self.nimi = nimi
        self.ikä = ikä
        self.taso = ""
        self.esineet = []
        self.nykyinen_sijainti = None

    def muuta_sanakirjaksi(self):
        return {
            "nimi": self.nimi,
            "ikä": self.ikä,
            "taso": self.taso,
            "esineet": self.esineet,
        }

    @classmethod
    def sanakirjasta(cls, data):
        pelaaja = cls(data["nimi"], data["ikä"])
        pelaaja.taso = data["taso"]
        pelaaja.esineet = data["esineet"]
        return pelaaja