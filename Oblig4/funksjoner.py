"""
Vi lager en funksjon som tar to heltall og returnerer summen av de to
tallene. Deretter kaller vi denne funksjonen to ganger.
Vi spor brukeren om aa oppgi en tekststreng og en bokstav.
Deretter skrvier vi en fuksjon som bruker for-lokke for aa
sjekke hvor mange ganger ble den oppgitte bokstaven brukt inn
i tekstestrengen. Vi legger til en til variabel count hver gang
bokstaven ble brukt i tekstrengen, og returnerer count.
"""

def adder(tall1, tall2):
    return tall1+tall2

sum1=adder(2,4)
sum2=adder(5,8)
print("Forste sum er ", sum1)
print("Andre sum er", sum2)

tekst=input("Oppgi en tekststreng: ")
bokstav=input("Oppgi en bokstav: ")

def tellForekomst(minTekst, minBokstav):
    count=0
    for tegn in minTekst:
        if tegn==minBokstav:
            count+=1
    return count

skrivut=tellForekomst(tekst, bokstav)
print("Din bokstav ble brukt i teksten din ", skrivut, "ganger")
