"""
Jeg lager en klasse med konstruktoren som tar imot alder og vekt; deretter setter
vi instansvariabler for disse verider. og lager en variabel til.
Deretter lager jeg 4 metoder:
1. metoden returnerer alder.
2. metoden returnerer vekt.
3. metoden misnker mattheten med en og bruker if-setning som minsker
vekten om mattheten er mindre enn 5
4. metoden tar imot et helltal og oker mettheten med dette helltalet.
Hvis mattheten er mer enn 7, da okes vektes med 1.
"""
class Hund:
    def __init__(self, alder, vekt):
        self._alder=alder
        self._vekt=vekt
        self._metthet=10

    def hentAlder(self):
        return self._alder

    def hentVekt(self):
        return self._vekt

    def spring(self):
        self._metthet-=1
        if self._metthet<5:
            self._vekt-=1

    def spis(self, heltall):
        self._metthet+=heltall
        if self._metthet>7:
            self._vekt+=1
