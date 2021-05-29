"""
Jeg lager et hovedprogram hvor jeg oppretter tre objekter. Deretter kaller Jeg
paa skrivUt metoden paa alle tre objektene, og kjor metoden paa det siste
objektet som oker kilometerstand med 10.
Deretter skriver jeg ut oppdatert kilometerstand.
"""

from motorsykkel import Motorsykkel

def hovedprogram():
    motor1=Motorsykkel("bmw", "9T8J", 125)
    motor2=Motorsykkel("audi", "3E45T", 240)
    motor3=Motorsykkel("yamaha", "O6Y54", 98)
    motor1.skrivUt()
    motor2.skrivUt()
    motor3.skrivUt()
    motor3.kjor(10)
    print(motor3.hentKilometerstand())

hovedprogram()
