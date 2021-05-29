class Node:
    def __init__(self, minne, antPros):
        self._minne=minne
        self._antPros=antPros

    def antProsessorer(self):
        return self._antPros

    def nokMinne(self, paakrevdMinne):
        return self._minne >=paakrevdMinne
