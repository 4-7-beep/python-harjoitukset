import random
import sys
import json
import time

PUNAINEN = "\033[91m"
VIHREA = "\033[92m"
KELTAINEN = "\033[93m"
SININEN = "\033[94m"
NOLLAA = "\033[0m"

TALLENNUS = "tallennus.json"

askel = random.randint(3,8)

def kävele(askel):
    print("Kävelet", end="", flush=True)
    for i in range(askel):
        time.sleep(0.5)
        if i % 2 == 0:
            print(" \u02D9", end="", flush=True)
        else:
            print(" .", end="", flush=True)
    print()

def tallenna_peli(pelaaja, sijainti):
    data = {
        "pelaaja": pelaaja.muuta_sanakirjaksi(),
        "sijainti": sijainti.muuta_sanakirjaksi(),
    }
    with open(TALLENNUS, "w", encoding="utf-8") as tiedosto:
        json.dump(data, tiedosto, ensure_ascii=False, indent=2)

def tulosta(teksti, pelaaja = None, väri="\033[93m"):
    print(väri + teksti + "\033[0m")
    print()
    jatko = input("\033[92mKävele - ENTER\nTallenna - kirjoita 'lopeta'\033[0m ")
    if jatko == "lopeta":
        tallenna_peli(pelaaja, sijainti)
        sys.exit()
    print()

class Sijainti:
    def __init__(self, nimi, alkutarina, alueen_kuvaus):
        self.nimi = nimi
        self.alkutarina = alkutarina
        self.alueen_kuvaus = alueen_kuvaus

    def pelaaja_saapuu(self, pelaaja):
        pelaaja.nykyinen_sijainti = self
        tulosta(self.alkutarina, pelaaja)
        tulosta(self.alueen_kuvaus, pelaaja)

class Tundra(Sijainti):
    def __init__(self):
        super().__init__(
        nimi="Siperian tundra",
        alkutarina="...",
        alueen_kuvaus="...",
        )

class Savanni(Sijainti):
    def __init__(self):
        super().__init__(
            nimi="Afrikan savanni",
            alkutarina="...",
            alueen_kuvaus="...",
        )

class Viidakko(Sijainti):
    def __init__(self):
        self.laskuri=0
        self.naru = False
        self.naru_redo = False
        self.siemen = False
        self.tapahtumat = [self.käärme, self.sade, self.villisika, self.joki,
                           self.salama, self.siemenet, self.heimo, self.lintu]
        super().__init__(
            nimi="viidakko",
            alkutarina=("Olit risteilylaivalla, jonka ruumassa tapahtui jokin räjähdys. "
                        "Laiva alkoi uppoamaan ja tipuit kannelta. "
                        "Ajauduit meren virran mukana kunnes saavuit saarelle."),
            alueen_kuvaus=("Olet hiekkarannalla ja edessäsi näkyy korkeita kookospuita. "
                           "Kaukana horisontissa on korkeita kukkuloita. "
                           "Taivaalla lentää muutamia eksoottisia lintuja."),
        )
    def muuta_sanakirjaksi(self):
        return {
        "laskuri": self.laskuri,
        "naru": self.naru,
        "siemen": self.siemen,
        "tapahtumat": [t.__name__ for t in self.tapahtumat],
        }

    def lataa_sanakirjasta(self, data):
        self.laskuri = data["laskuri"]
        self.naru = data["naru"]
        self.luola_tutkittu = data["luola_tutkittu"]
        self.tapahtumat = [getattr(self, nimi) for nimi in data["tapahtumat"]]

    def random_tapahtuma(self, pelaaja):
        if not self.tapahtumat:
            return 

        tapahtuma = random.choice(self.tapahtumat)
        self.tapahtumat.remove(tapahtuma)
        kävele(askel)
        tapahtuma(pelaaja)
    

        self.laskuri += 1
        if self.laskuri == 3:
            kävele(askel)
            self.luola(pelaaja)
        if self.laskuri == 6:
            kävele(askel)
            self.pressu(pelaaja)
        if self.laskuri == 8:
            print("Et halunnut rakentaa lauttaa ja jäit viidakkoon asumaan.")

    def lintu(self, pelaaja):
        tulosta("Viereesi laskeutuu hieno lintu, joka laulaa kauniisti")
        if self.siemen:
            tarjoa = input("Haluatko tarjota linnulle löytämiäsi siemeniä\n1: Kyllä\n2: Ei\n1-2: ")
            if tarjoa == "1":
                tulosta("Tarjosit linnulle siemeniä ja ne näyttää maistuvan, teit linnusta ystäväsi :)")
        else:
            tulosta("Sinulla ei ole mitään tarjottavaa linnulle ja se lentää pois")

    def heimo(self, pelaaja):
        tulosta("Näet viidakossa kymmeniä ihmisiä, jotka vaikuttavat asuvan saarella")
        tulosta("IHMISET NÄKIVÄT SINUT JA ALKOIVAT JUOSTA SINUA KOHTI")
        hätä = input("1: Juokse\n2: Pysy paikallasi\n1-2: ")
        if hätä == "1":
            tulosta("Pääsit ihmisiä karkuun vähän matkaa, mutta he olivat nopeampia ja saivat sinut kiinni")
            tulosta("Ihmiset vievät sinut heidän leirilleen ja valmistelevat nuotiota")
            hätä2 = input("1: Yritä tehdä ihmisiin vaikutus\n2: Älä tee mitään\n1-2: ")
            if hätä2 == "1":
                tulosta("Aloit piirtämään kallion seinämään kuvia ja ihmiset vaikuttuivat taiteestasi")
                tulosta("Ihmiset päästävät sinut lähtemään")
        elif hätä == "2":
            tulosta("Ihmiset vievät sinut heidän leirilleen ja valmistelevat nuotiota")
            tulosta("Ihmiset alkavat hieroa sinuun jotakin öljyä ja nostavat sinut nuotion päälle")
            tulosta("Ihmiset söivät sinut. Hävisit pelin.")
            sys.exit()

    def pressu(self, pelaaja):
            tulosta("Näet maassa pressun, joka vaikuttaisi olevan ehjä. Voit käyttää löytämääsi narua tehdäksesi lautan")
            if self.naru:
                tulosta("Sinulla on narua ja pressu, voit rakentaa lautan")
                tulosta("Onnistuit rakentamaan lautan ja pääsit merellä niin pitkälle, että rahtilaiva näki ja pelasti sinut")
                sys.exit()
            else:
                naru_redo = input("Jätit narun luolaan, haluatko mennä hakemaan sen?\n1: Kyllä\n2: Ei\n1-2: ")
                if naru_redo == "1":
                    self.luola(pelaaja)
                    tulosta("Sinulla on narua ja pressu, voit rakentaa lautan")
                    tulosta("Onnistuit rakentamaan lautan ja pääsit merellä niin pitkälle, että rahtilaiva näki ja pelasti sinut")
                    sys.exit()

    def luola(self, pelaaja):
        tulosta("Näet edessäsi ison luolan")
        luola = input("Haluatko mennä tutkimaan?\n1: Kyllä\n2: Ei\n1-2: ")
        if luola == "1":
            tulosta("Luolassa on kosteaa ja hämärää, mutta auringonvalo valaisee tarpeeksi, että näet")
            naru = input("Näet maassa ison kasan narua, otatko sen mukaasi?\n1: Kyllä\n2: Ei\n1-2: ")
            tulosta("Luolassa ei näyttänyt olevan muuta ja lähdit")
            if naru == "1":
                self.naru = True
                self.naru_redo = True
        
    def käärme(self, pelaaja):
        tulosta("Käärme sihisee jalkojesi juuressa!")
        valinta = input("Ajattele nopeasti:\n"
                        "1: Juokse\n2: Huuda\n1-2: ")
        if valinta == "1":
            tulosta("Kompastuit juostessasi puun kantoon, mutta et näe käärmettä enää, olet turvassa toistaiseksi")
        elif valinta == "2":
            tulosta("Käärme säikähti huutoasi ja liukerteli pois")

    def sade(self, pelaaja):
        tulosta("Alkoi satamaan kaatamalla, kannattaa yrittää kerätä vettä")
        keräys = input("Miten yrität kerätä vettä:\n1: Tekemällä käsistäsi kupin\n2: Käyttämällä puiden lehtiä ohjataksesi veden\n3: Seisot suu auki ja toivot veden osuvan hyvin\n1-3: ")
        if keräys == "1":
            tulosta("Sait juotua janon pois nyt, mutta sinulla ei ole vettä jatkoa varten")
        elif keräys == "2":
            tulosta("Sait kerättyä vettä tarpeeksi juodaksesi nyt ja myöhemmin")
        elif keräys == "3":
            tulosta("Sait valitettavasti vain muutamia tippoja suuhusi ja janosi ei lähtenyt")

    def villisika(self, pelaaja):
        tulosta("Villisika ryntää pusikosta suoraan sinua päin!!!")
        teko = input("Mitä teet?\n1: Kiipeä puuhun\n2: Seiso paikallasi\n1-2: ")
        if teko == "1":
            tulosta("Kiipesit puuhun ja odotit kunnes villisika lähti")
        elif teko == "2":
            tulosta("Villisika hämmentyi liikkumattomuudestasi ja lähestyikin sinua ystävällisemmin. Sait villisiasta kaverin :)")

    def joki(self, pelaaja):
        tulosta("Saavuit ison joen luo, joudut joko kiertämään pitkän matkan tai yrittää uida yli")
        joki = input("1: Ui yli\n2: Kierrä joen ympäri\n1-2: ")
        if joki == "1":
            tulosta("Ajauduit virran mukana ja sait haavoja osuessasi kiviin")
        elif joki == "2":
            tulosta("Kiersit joen ympäri, mutta pitkä matka alkoi janottamaan")

    def salama(self, pelaaja):
        tulosta("Yhtäkkiä ukkonen alkaa jyrisemään ja salamoita iskee lähellesi")
        salama = input("1: Uhmaatko onneasi?\n2: Mene suojaan\n1-2: ")
        if salama == "1":
            tulosta("Salama iskee erittäin lähelle sinua ja juoksit turvaan. ÄLÄ KOETTELE ONNEA")
        elif salama == "2":
            tulosta("Menit suojaan ja odotit, kunnes ukkonen häipyi")

    def siemenet(self, pelaaja):
        tulosta("Löysit mystisen pussin erilaisia siemeniä, haluatko istuttaa niitä?")
        siemen = input("1: Kyllä\n2: Ei\n1-2: ")
        if siemen == "1":
            self.siemen = True
            tulosta("Istutit siemeniä ja edesautit kestävää kehitystä saarella")