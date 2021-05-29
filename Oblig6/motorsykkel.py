"""
Jeg lager en klasse med konstruktoren som tar imot merke, registreringsnummer
og kilometerstand, og setter instansvariabler til disse veridene.
Deretter lager jeg 3 metoder:
1. metoden tar imot antall kilometer og oker kilometerstand med dette antallet.
2. metoden returnerer kilometerstand
3. metoden skriver ut instansvariablene.
"""

class Motorsykkel:
    def __init__(self, merke, registreringsnummer,kilometerstand):
        self._merke=merke
        self._registreringsnummer=registreringsnummer
        self._kilometerstand=kilometerstand

    def kjor(self, km):
        self._kilometerstand+=km

    def hentKilometerstand(self):
        return self._kilometerstand

    def skrivUt(self):
        print(self._merke)
        print(self._registreringsnummer)
        print(self._kilometerstand)
