"""
Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.
"""

talvi = (12, 1, 2)
kevät = (3, 4, 5)
kesä = (6, 7, 8)
syksy = (9, 10, 11)

kuukausi = int(input("Anna kuukauden numero: "))
if kuukausi in talvi:
    print("talvi")
elif kuukausi in kevät:
    print("kevät")
elif kuukausi in kesä:
    print("kesä")
elif kuukausi in syksy:
    print("syksy")