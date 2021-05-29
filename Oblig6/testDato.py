"""
Jeg lager en hovedprogram hvor vi oppretter et objekt.
Deretter skriver vi ut hvilken aar det er i datoen.
Vi bruker if-setning  og sjekkDato metoden for aa sjekke om dagen ble oppgitt
er lik 15 eller 1, og skriver ut teksten.
Deretter skriver vi ut datoen paa brukervenlig maaten og kaller paa metoden
som endrer datoen; etter det skriver vi ut datoen paa nytt.
Siste: kaller vi paa nyDato metoden.
"""

from dato import Dato

def hovedprogram():
    date=Dato(15,10,2020)
    print("Datoens aar er", date.hentAaret())
    if date.sjekkDato(15)==True:
        print("Loenningsdag!")
    elif date.sjekkDato(1)==True:
        print("Ny maaned, nye muligheter!")

    print(date.lagStreng())
    date.endreDato()
    print(date.lagStreng())
    date.nyDato()


hovedprogram()
