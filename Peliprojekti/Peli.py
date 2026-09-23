nimi = input("Anna nimesi: ")
ikä = int(input("Anna ikäsi: "))

if ikä < 12:
    print("Olet alaikäinen, etkä voi pelata peliä")
else:
    print("Terve " + nimi + "!")

import json

def tallenna_peli(pelaaja):
    with open("tallennus.json", "w", encoding="utf-8") as tiedosto:
        json.dump(pelaaja, tiedosto)

def lataa_peli():
    try:
        with open("tallennus.json", "r", encoding="utf-8") as tiedosto:
            return json.load(tiedosto)
    except FileNotFoundError:
        return None

lataus = lataa_peli()

with open("intro.txt", "r", encoding="utf-8") as tiedosto:
    data = tiedosto.read()
    print(data)

alku = input("Lue ohjeita kirjoittamalla 'ohje', jatka kirjoittamalla 'jatka' tai lataa vanha tallennus kirjoittamalla 'lataa' ")
if alku == "ohje":
    with open("ohjeet.txt", "r", encoding="utf-8") as tiedosto:
        data1 = tiedosto.read()
        print(data1)
elif alku == "lataa":
    if nimi in lataus:
        tila = lataus[nimi]
elif alku == "jatka":
    pass

päävalikko = ["1. Pelaa peliä", "2. Maailman valikko", "3. Lopeta peli"]

esineet = ["1. Kirves", "2. Keihas", "3. Vesipullo", "4. Tulukset", "5. Taskulamppu"]

lokaatio = ["1. Amazonin sademetsä", "2. Siperian tundra", "3. Afrikan savanni"]

inventaario = []

def lokaatio_valinta():
    for l in lokaatio:
        print(l)
    lokaatio_valinta_input = int(input("Valitse lokaatio 1-3: "))
    inventaario_lokaatio = lokaatio[lokaatio_valinta_input - 1]
    inventaario.append(inventaario_lokaatio)

def esine_valinta():
    for e in esineet:
        print(e)
    esine_valinta_input = int(input("Valitse yksi esine 1-5: "))
    inventaario_esine = esineet[esine_valinta_input - 1]
    inventaario.append(inventaario_esine)

def info():
    print(inventaario)

for p in päävalikko:
    print(p)
valinta = input("Valitse vaihtoehto (1-3): ")

if valinta == "1":
    print("Peli alkaa!")
elif valinta == "2":
    lokaatio_valinta()
    esine_valinta()
    for p in päävalikko:
        print(p)
    valinta = input("Valitse vaihtoehto (1-3): ")
    if valinta == "1":
        print("Peli alkaa!")
elif valinta == "3":
    print("Lopetit pelin.")






