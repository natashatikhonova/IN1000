#Denne klasse lager en celle
class Celle:
    #konstruktoeren som oppretter cellen med status doed
    def __init__(self):
        self._status='doed'
    #metoden som setter status til cellen til doed
    def settDoed(self):
        self._status='doed'
    #metoden som setter status til cellen til levende
    def settLevende(self):
        self._status='levende'
    #metoden bruker if-setning for aa sjekke status til cellen og returnerer status
    def erLevende(self):
        if self._status=='levende':
            return True
        else:
            return False
    #metoden returnerer en tegnerepresentasjon av cellens status
    def hentStatusTegn(self):
        if self.erLevende():
            return 'O'
        else:
            return '.'
