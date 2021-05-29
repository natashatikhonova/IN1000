"""
Jeg lager et hoverprogram hvor jeg oppretter et objekt og kaller paa
metdene spring og spis 2 ganger hver, og skriver ut vekten etter hver gang
jeg kaller paa metoden.
"""

from hund import Hund

def hovedprogram():
    babyHund=Hund(1, 5)
    babyHund.spring()
    print(babyHund.hentVekt())
    babyHund.spis(1)
    print(babyHund.hentVekt())
    babyHund.spring()
    print(babyHund.hentVekt())
    babyHund.spis(2)
    print(babyHund.hentVekt())

hovedprogram()
