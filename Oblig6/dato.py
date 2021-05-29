"""
Jeg lager en klasse som representerer dato. I konstruktoren skal vi ta imot
dag, maaned og aar og deretter oppretter vi instansvariabler.
Jeg lager forskjellige metoder innefor klassen:
1. metoden returnerer aar.
2. metoden tar instansvariablene, gjor dem til en streng og returnerer
den paa brukervenlig maaten
3. metoden tar imot et heltall, og hvis dette heltallet er like dagen (instansvaribel),
da returnerer den True
4. metoden tar input bra brukeren (ny dato), bruker funksjon split for
aa dele strengen og legger elementene til listen.
Deretter sammenligner den maaneder, aar og dager for aa finne hvilken
dato kommer forst.
5. metoden sjekker om datoen faller paa siste dagen om maaneden (avhengig
av hvor mange dager det er i hver eneste maaned). Hvis det er siste dag,
da oker programmet maaned med 1, og forandrer verdi paa dag til 1.
Hvis det er ikke siste dag, da oker programmet dagen med 1.

"""
class Dato:
    def __init__(self, nyDag, nyMaaned, nyttAar):
        self._dag=int(nyDag)
        self._maaned=int(nyMaaned)
        self._aar=int(nyttAar)

    def hentAaret(self):
        return self._aar

    def lagStreng(self):
        dato=str(str(self._dag)+"."+str(self._maaned)+"."+str(self._aar))
        return dato

    def sjekkDato(self, bestemtDag):
        if self._dag==bestemtDag:
            return True

    def nyDato(self):
        datoFraBruker=input("Skriv inn dato (eks. (16.10.2020): )")
        date=datoFraBruker.split(".")
        if int(date[2])>self._aar:
            print("Ny dato kommer etter foerste dato.")
        elif int(date[1])>self._maaned:
            print("Ny dato kommer etter foerste dato.")
        elif int(date[1])==self._maaned:
            if int(date[0])>self._dag:
                print("Ny dato kommer etter foerste dato.")
        else:
            print("Ny dato kommer foer foerste dato")

    def endreDato(self):
        if (self._maaned==2 and self._dag==28) or ((self._maaned==4 or self._maaned==6 or self._maaned==9 or self._maaned==11) and self._dag==30) or ((self._maaned==1 or self._maaned==3 or self._maaned==5 or self._maaned==7 or self._maaned==8 or self._maaned==10 or self._maaned==12) and self._dag==31):
            self._dag==1
            self._maaned+=1
        else:
            self._dag+=1
