import rack from Rack

class Regneklynge:
    def __init__(self, noderPerRack):
        self._racks=[]
        if noderPerRack>0:
            self._noderPerRack=noderPerRack
        else:
            self._noderPerRack=1

    def settInnNode(self, node):
        ledigRack=None
        i = 0

        while ledigRack == None and i<len(self._racks):
            if self._racks[i].getAntNoder()<self._noderPerRack:
                ledigRack=self._racks[i]
            i+=1

        if ledigRack == None:
            ledigRack=Rack()
            self._racks.append(ledigRack)
        ledigRack.settInn(node)


    def antProsessorer(self):
        antPros=0
        for rack in self._racks:
            antPros+=rack.antProsessorer()
        return antPros

    def noderMedNokMinne(self, paakrevdMinne):
        antNoder=0
        for rack in self._racks:
            antNoder+=rack.noderMedNokMinne(paakrevdMinne)
        return antNoder

    def antRacks(self):
        return len(self._racks)
