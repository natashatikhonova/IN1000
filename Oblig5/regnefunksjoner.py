"""
Forst skriver jeg en funksjon som tar imot to tall og returnerer summen av dem.
Deretter skriver jeg to funksjoner til som tar imot to tall og returnerer
1. subtraksjonen av dem
2. divisjonen av dem

Jeg bruker assert for aa teste alle tre funksjonene paa tre forskjellige maater.
Deretter skrever jeg en funksjon som tar imot et tall og returnerer
dette tallet*2.54 (tommer til cm). Funksjonen sjekker om tallet som ble
oppgitt er positivt.

Jeg skriver en prosedyre som tar to inputer fra brukeren og kaller paa de
overste funksjonene med disse to tall som argument.

"""
def addisjon(tall1, tall2):
    return tall1+tall2

def subtraksjon(tall1, tall2):
    return tall1-tall2

def divisjon(tall1, tall2):
    return tall1/tall2

assert addisjon(14,24) == 38
assert addisjon(13, -5) == 8
assert addisjon(-10, -11) == -21

assert subtraksjon(25, 11) == 14
assert subtraksjon(30, -9) == 39
assert subtraksjon(-3, -8) == 5

assert divisjon(12, 4) == 3
assert divisjon(25, -5)== -5
assert divisjon(-48, -8) == 6

def tommerTilCm(antallTommer):
    assert antallTommer>0
    return antallTommer*2.54

def skrivBeregninger():
    print("Utregninger:")
    tall1=float(input("Skriv inn tall 1: "))
    tall2=float(input("Skriv inn tall 2: "))
    print("Resultat av summering: ", addisjon(tall1, tall2))
    print("Resultat av subtraksjon: ", subtraksjon(tall1, tall2))
    print("Resultat av divisjon: ", divisjon(tall1, tall2))
    print("Konvertering fra tommer til cm: ")
    tall=float(input("Skriv inn et tall: "))
    print("Resultat: ", tommerTilCm(tall))

skrivBeregninger()
