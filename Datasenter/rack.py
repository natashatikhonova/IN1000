import node from Node
class Rack:
    def __init__(self):
        self._noder=[]

    def settInn(self, node):
        self._noder.append(node)

    def getAntNoder(self):
        return len(self._noder)

    def antProsessorer(self):
        antPros=0
        for node in self._noder:
            antPros+=node.antProsessorer()
        return antPros

    def noderMedNokMinne(self, paakrevdMinne):
        antNoder= 0
        for noder in self._noder:
            if node.nokMinne():
                antNoder+=1
        return antNoder
