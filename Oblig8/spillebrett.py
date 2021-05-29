#Denne klassen lager et todimensjonalt brett som inneholder celler
import random
from celle import Celle

class Spillebrett:
    # konstruktoeren som tar imot antall rader og kolonner, og lager et brett med celler og genererer det
    def __init__(self, rader, kolonner):
        self._rader=rader
        self._kolonner=kolonner
        self._rutenett=[
            [Celle()
            for celler in range(self._kolonner)]
            for celler in range(self._rader)]
        self._generasjonsnummer=0
        self._generer()

    #metoden bruker for-loekke for aa gaa gjennom brettet og setter status til 1/3 av celler til levende
    def _generer(self):
        for rad in self._rutenett:
            for kolonne in rad:
                randomSjanse=random.randint(0,2)
                if randomSjanse==0:
                    kolonne.settLevende()

    #metoden bruker for-loekke for aa gaa gjennom alle cellene og henter tegnerepresentasjon fra klassen Celle og skriver den ut
    def tegnBrett(self):
        print('\n')
        for rad in self._rutenett:
            for kolonne in rad:
                print(kolonne.hentStatusTegn(), end='')
            print()

    #metoden tar imot cellens koorinater og returnerer en liste med alle cellens naboer
    def finnNabo(self, rad, kolonne):
        listeAvNaboer=[]

        #iterer over alle naboene
        for i in range(-1, 2):
            for j in range(-1,2):
                radTilNabo=rad+i
                kolonneTilNabo=kolonne+j

                nabo=True

                if radTilNabo==rad and kolonneTilNabo==kolonne:
                    nabo=False

                #radTilNabo er utenfor indeksene sine
                if radTilNabo<0 or radTilNabo>=self._rader:
                    nabo=False

                #kolonneTilNabo er utenfor indeksene sine
                if kolonneTilNabo<0 or kolonneTilNabo>=self._kolonner:
                    nabo=False

                #legge til listen
                if nabo:
                    listeAvNaboer.append(self._rutenett[radTilNabo][kolonneTilNabo])

        return listeAvNaboer

    #denne metoden oppdaterer brettet
    def oppdatering(self):
        #oppretter to lister for 1. alle levende celler; 2. alle doede celler
        alleLevende=[]
        alleDoede=[]

        #gaar gjennom alle cellene ved bruk av for-loekke og finner naboer til cellen
        for i in range(len(self._rutenett)):
            for j in range(len(self._rutenett[i])):
                sjekkeNabo=self.finnNabo(i, j)

                #oppretter liste med som teller levende nabocellene
                tellerAvLevendeCeller=[]
                # gaar gjennom alle nabocellene og legger alle levende celler til listen
                for nabocelle in sjekkeNabo:
                    if nabocelle.erLevende():
                        tellerAvLevendeCeller.append(nabocelle)

                #henter naavaerende status av cellen
                nyCelle=self._rutenett[i][j]
                status=nyCelle.erLevende()

                #hvis cellen er levende:
                if status==True:
                    #og antall levende naboer er mindre enn 2 og stoerre enn 3, settes cellen til doed
                    if len(tellerAvLevendeCeller)<2 or len(tellerAvLevendeCeller)>3:
                        alleDoede.append(nyCelle)
                    #og antall levende naboer er lik 2 eller 3, settes cellen til levende
                    if len(tellerAvLevendeCeller)==3 or len(tellerAvLevendeCeller)==2:
                        alleLevende.append(nyCelle)
                #hvis cellen er doed:
                else:
                    #og antall levende naboer lik 3, settes cellen til levende
                    if len(tellerAvLevendeCeller)==3:
                        alleLevende.append(nyCelle)

        #setter alle cellene i listen alleLevende til status levende
        for elementer in alleLevende:
            elementer.settLevende()
        #setter alle cellene i listen alleDoede til status doed
        for elementer in alleDoede:
            elementer.settDoed()

        #oppdaterer telleren for antall generasjoner
        self._generasjonsnummer+=1

    #metoden gaar gjennom alle cellene ved bruk av for-loekken; hvis celle er levende, da oeker teller med 1
    def finnAntallLevende(self):
        teller=0
        for rad in self._rutenett:
            for kolonne in rad:
                if kolonne.erLevende():
                    teller+=1
        return teller
