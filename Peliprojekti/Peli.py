nimi = input("Anna nimesi: ")
ikä = int(input("Anna ikäsi: "))

if ikä < 12:
    print("Olet alaikäinen, etkä voi pelata peliä")
else:
    print("Terve " + nimi + "!")

päävalikko = """
1. Pelaa peliä
2. Maailman valikko
3. Lopeta
"""

esineet = """
1. Kirves
2. Keihas
3. Vesipullo
4. Tulukset
5. Taskulamppu
"""

while True:
    print(päävalikko)
    valinta = input("Valitse vaihtoehto (1-3): ")


    if valinta == "1":
        print("Peli alkaa!")
    elif valinta == "2":
        print(esineet)
        input("Valitse yksi esine mukaasi: ")
    elif valinta == "3":
        print("Lopetit pelin.")
        break

