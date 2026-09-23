"Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm."

kuhan_pituus = input("Anna kuhan pituus senttimetreinä: ")
if kuhan_pituus != 37:
    alimitta = 37 - float(kuhan_pituus)
    print(f"Laske kuha takaisin, se on alimittainen " + str(alimitta)[:4] + " sentillä")