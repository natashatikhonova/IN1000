'''
Denne klassen har konstruktoer som har 2 instansvariabler:
en liste med sanger og navn paa listen.
'''
from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

#denne metoden gaar gjennon sangene i spillelisten og gjor alle til brukervenlig streng
    def __str__(self):
        streng = ''
        for sang in self._sanger:
            streng += str(sang)

        return streng

#denne metoden tar imot filnavn, leser filen og gaar gjennom alle
#linjene i filen og oppretter nye Sang-objekter og legger dem inn i spillelisten
    def lesFraFil(self, filnavn):
        fil=open(filnavn, "r")
        for linje in fil:
            alleData=linje.strip().split(';')
            sang=Sang(alleData[1], alleData[0])
            self._sanger.append(sang)
        fil.close()

#denne metoden tar imot nySang og legger den til spillelisten
    def leggTilSang(self, nySang):
        self._sanger.append(nySang)

#denne metoden tar imot sang og fjerner den fra spillelisten
    def fjernSang(self, sang):
        self._sanger.remove(sang)

#denne metoden tar imot en sang ob bruker metoden spill for aa spille en sang
    def spillSang(self, sang):
        sang.spill()

#denne metoden gaar gjennom alle sangene i spillelisten og spiller alle sangene
    def spillAlle(self):
        for hver in self._sanger:
            hver.spill()

#denne metoden tar imot tittel og gaar gjennom alle sangene i spillelisten
#sjekker om den oppgitte tittel er lik tittelen av noen av de sangene i spillelisten
#bruker metoden sjekkTittel for aa sjekke tittelen
    def finnSang(self, tittel):
        for element in self._sanger:
            if element.sjekkTittel(tittel):
                return element
        return None

#denne metoden tar imot artistnavn, oppretter en tom liste og gaar gjennom alle sangene i spillelisten
#bruker metoden sjekkArtist for aa sjekke om spillelisten inneholder sangene av denne artist
#om metoden er lik True, returnerer metoden alle sangene fra denne artisten
    def hentArtistUtvalg(self, artistnavn):
        sangerFraArtist=[]
        for sang in self._sanger:
            if sang.sjekkArtist(artistnavn)==True:
                sangerFraArtist.append(sang)

        return sangerFraArtist
