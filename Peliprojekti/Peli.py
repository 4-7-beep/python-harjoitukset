import json
import os
import sys
from Sijainti import Viidakko, Tundra, Savanni
from Sijainti import tulosta, tallenna_peli
from Pelaaja import Pelaaja

viidakko = Viidakko()

SIJAINNIT = {
    "Viidakko": Viidakko,
    "Siperian tundra": Tundra,
    "Afrikan savanni": Savanni
}

TALLENNUS = "tallennus.json"

päävalikko = ["1. Pelaa peliä", "2. Maailman valikko", "3. Lopeta peli"]
esineet = ["Kirves", "Keihäs", "Vesipullo", "Tulukset", "Taskulamppu"]

# Värikoodit

PUNAINEN = "\033[91m"
VIHREA = "\033[92m"
KELTAINEN = "\033[93m"
SININEN = "\033[94m"
NOLLAA = "\033[0m"

# Pelin toimivuuden kannalta tärkeät funktiot

def lataa_peli():
    if not os.path.exists(TALLENNUS):
        return None
    try:
        with open(TALLENNUS, "r", encoding="utf-8") as tallennus:
            return json.load(tallennus)
    except json.JSONDecodeError:
        print("Tallennustiedosto on rikki.")
        return None


def valitse(otsikko, vaihtoehdot):
    for i, v in enumerate(vaihtoehdot, 1):
        print(f"{i}. {v}")
    while True:
        try:
            n = int(input(f"{otsikko} (1-{len(vaihtoehdot)}): "))
            if 1 <= n <= len(vaihtoehdot):
                return vaihtoehdot[n - 1]
        except ValueError:
            pass
        print("Virheellinen valinta, yritä uudelleen.")

# Aloitusvalikko

pelaaja = None
while pelaaja is None:
    alku = input("Lue ohjeita kirjoittamalla 'ohje'\n"
                 "Aloita uusi peli kirjoittamalla 'jatka'\n"
                 "Lataa vanha tallennus kirjoittamalla 'lataa': ")

    if alku == "ohje":
        with open("ohjeet.txt", "r", encoding="utf-8") as f:
            print(f.read())
    elif alku == "lataa":
        pelaaja = lataa_peli()
        if pelaaja is None:
            print("Tallennusta ei löytynyt.")
        else:
            print(f"Tervetuloa takaisin, pelaaja.nimi!")
    elif alku == "jatka":
        nimi = input("Anna nimesi: ")
        while True:
            try:
                ikä = int(input("Anna ikäsi: "))
                break
            except ValueError:
                print("Anna ikä numerona.")
        if ikä < 12:
            print("Olet alaikäinen, etkä voi pelata peliä")
            sys.exit()
        print(f"Terve {nimi}!")
        pelaaja = Pelaaja(nimi, ikä)
    else:
        print("Et antanut oikeaa komentoa, kokeile uudestaan.")

# Päävalikko

while True:
    for p in päävalikko:
        print(p)
    valinta = input("Valitse vaihtoehto (1-3): ")
    print()

    if valinta == "1":
        if sijainti is None or not pelaaja.esineet:
            print("Valitse ensin lokaatio ja esine maailman valikosta.")
        else:
            tulosta("Peli alkaa!")
            sijainti.pelaaja_saapuu(pelaaja)


            while True:
                sijainti.random_tapahtuma(pelaaja)

    if valinta == "2":
        valittu = valitse("Valitse lokaatio", list(SIJAINNIT.keys()))
        pelaaja.taso = valittu
        sijainti = SIJAINNIT[valittu]()

        pelaaja.esineet = [valitse("Valitse esine", esineet)]
        tallenna_peli(pelaaja, sijainti)
        print("Valinnat tallennettu.")

    elif valinta == "3":
        tallenna_peli(pelaaja, sijainti)
        print("Lopetit pelin.")
        break

    else:
        print("Virheellinen valinta.")