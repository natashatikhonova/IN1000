'''
Jeg skriver en klasse Sang som har en konstruktoer som
har parametere for tittel og artist og oppretter instansvariablene
tittel og artist.
'''
class Sang:
    def __init__(self, artist, tittel):
        self._tittel=tittel
        self._artist=artist

#denne metoden returnerer streng av tittel og artist paa menneskevennlig maate
    def __str__(self):
        return f"{self._tittel} av {self._artist}  "
#denne metoden spiller sangen og skriver ut til terminalen informasjon om sangen som spilles
    def spill(self):
        print("Spiller", self)

#denne metoden har parameter navn og sjekker om det oppgitte navnet er lik ett eller flere ord i artistens navn
#metoden gaar inn i for-loekke for aa gaa gjennom alle ord i artist
    def sjekkArtist(self, navn):
        for ord in navn.split():
            if ord in self._artist.split():
                return True
        return False
#denne metoden har parameter tittel og sjekker om det oppgitte tittel er lik instansvariabel tittel
#jeg bruker funksjon lower() og if-setning for aa se om tittlene er like uavhengig av store/smaa bokstaver
    def sjekkTittel(self, tittel):
        tittel=tittel.lower()
        self._tittel=self._tittel.lower()
        if tittel==self._tittel:
            return True
        return False

#denne metoden har parametere artist og tittel og bruker if-setning
#for aa se om metodene sjekkArtist og sjekkTittel er lik True med de oppgitte parametere
#hvis begge er True, da returnerer metoden True

    def sjekkArtistOgTittel(self, artist, tittel):
        if self.sjekkArtist(artist)==True and self.sjekkTittel(tittel)==True:
            return True
        else:
            return False
