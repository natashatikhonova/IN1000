from regneklynge import Regneklynge
class Datasenter:
    def __init__(self):
        self._regneklynger={}

    def lesInnRegneklynge(self, filnavn):
        fil=open(filnavn, 'r')
        navn=filnavn.split(".")[0]
        noderPerRack=int(fil.readline().strip())
        regneklynge=Regneklynge(noderPerRack)
        self._regneklynger[navn]= regneklynge

        for linje in fil:
            data=linje.strip().split()
            for i in range(0, int(data[0])):
                node=Node(data[1], data[2])
                regneklynge.settInnNode(node)

        fil.close()


    def skrivUtAlleRegneklynger(self):
        for navn in self._regnklynger:
            skrivUtRegneklynge(navn)


    def skrivUtRegneklynge(self, navn):
        if navn in self._regneklynger:
            regneklynge= self._regneklynger[navn]
            print(navn, "har", self._regneklynger[navn].antRacks(), "racks")
            print("Noder med minst 32GB:", regneklynge.noderMedNokMinne(32))
            print("Noder med minst 64GB:", regneklynge.noderMedNokMinne(64))
            print("Noder med minst 128GB:", regneklynge.noderMedNokMinne(128))
        else:
            print("Det finnes ingen regneklynge med dette navnet i datasenteret")
