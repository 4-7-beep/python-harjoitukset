"""
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.
"""

luvut = []

luku = input("Anna luku tai lopeta painamalla ENTER: ")
while luku != "":
    lukuInt = int(luku)
    luvut.append(lukuInt)
    luku = input("Anna luku tai lopeta painamalla ENTER: ")


luvut.sort(reverse=True)
for i in luvut[0:5]:
    print(i)

           