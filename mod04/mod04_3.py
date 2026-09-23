"""
Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l. 
"""

käyttäjä = input("Mikä on biologinen sukupuolesi? ").lower()
hemoglobiini = int(input("Mikä on hemoglobiiniarvosi? "))

if käyttäjä == "nainen" and 117 <= hemoglobiini <= 175:
    print("Hemoglobiiniarvosi ovat normaalit.")
elif käyttäjä == "nainen" and hemoglobiini < 117:
    print("Hemoglobiiniarvosi ovat alhaiset.")
elif käyttäjä == "nainen" and hemoglobiini > 175:
    print("Hemoglobiiniarvosi ovat korkeat.")

if käyttäjä == "mies" and 134 <= hemoglobiini <= 195:
    print("Hemoglobiiniarvosi ovat normaalit.")
elif käyttäjä == "mies" and hemoglobiini < 134:
    print("Hemoglobiiniarvosi ovat alhaiset.")
elif käyttäjä == "mies" and hemoglobiini > 195:
    print("Hemoglobiiniarvosi ovat korkeat.")