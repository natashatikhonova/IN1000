"""
Jeg lager en klasse Person som tar imot navn og alder og oppretter instansvariabler
med disse; og konstruktoren oppretter en til variabel som er tom liste.
Deretter lager jeg tre metoder:
1. metode tar imot en tekststreng og legger den til listen.
2. metoden bruker for-lokke for aa skrive ut alle elementene i listen.
3. metoden skriver ut navn, alder og kaller paa 2. metoden.
"""

class Person:
    def __init__(self, navn, alder):
        self._navn=navn
        self._alder=alder
        self._hobbyer=[]

    def leggTilHobby(self, hobby):
        self._hobbyer.append(hobby)

    def skrivHobbyer(self):
        print("Dine hobbyer er :")
        for element in self._hobbyer:
            print(element)

    def skrivUt(self):
        print("Ditt navn er", self._navn)
        print("Du er ",self._alder, "aar gammel")
        self.skrivHobbyer()

"""
Jeg lager et hovedprogram hvor jeg tar innput fra brukeren
og oppretter et objekt med disse argumentene.
Deretter gaar jeg inn i en while-lokke for aa spore brukeren om input.
Hver input legges til hobbyliste. Hvis bruker ikke onsker aa oppgi mer,
da avsluttes lokke og programmet kaller paa 3. metode (skriv ut)
"""


def hovedprogram():
    name=input("Skriv inn navnet ditt: ")
    age=input("Hvor gammel er du? : ")
    nyPerson=Person(name, age)
    svar="ja"

    while svar=="ja":
        nyHobby=input("Skriv din hobby: ")
        nyPerson.leggTilHobby(nyHobby)
        svar=input("Har du lyst aa legge til mer hobbyer?: ").lower()

    nyPerson.skrivUt()

hovedprogram()
