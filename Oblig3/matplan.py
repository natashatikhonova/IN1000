"""
Dette programmet lager først en ordbok med en liste inn i hver nøkkelverdi med navn av beboere og deres matplan.
Deretter bruker vi en funksjon for aa skrive ut navn paa alle beboere da kan brukeren taste inn et navn fra listen.
Naar brukeren gjor det, faar den oversikt over matplanen til den enkelte beboeren. Hvis dette navnet er ikke registrert, faar
brukeren en feil melding.
"""
matplan={"Ole Petersen":["brod til frokost", "egg til lunsj", "kylling til middag"],
"Marte Johansen":["egg til frokost", "salat til lunsj", "suppe til middag"],
"Svein Bo":["havregryn til frokost", "taco til lunsj", "pasta til middag"]}

def beboer():
    print(matplan.keys())
    navn=input("Skriv inn navnet til en beboer: ")
    if navn in matplan:
        plan=matplan[navn]
        print("Matplan til",navn, "er",plan)
    else:
        print("Denne beboeren er ikke registrert!")

beboer()

"""
Deloppgave 3:
a. For aa representere brukernavn paa alle IN1000 studentene ville jeg bruke megnden. Siden alle IN1000 studentene har forskjellige brukernavn
er det lurt aa bruke mengden slik brukernavn blir ikke brukt mer enn en gang.

b. For aa representere brukernavn og antall poeng paa innlevering 3 for alle studentene paa IN1000 ville jeg bruke ordbok. Det er besste maaten aa
representere informasjon i denne situasjonen siden det er baade brukernavn og antall poeng som blir registrert. Ved bruk av ordbok faar vi
ordentlig oversikt av alle studentene og poengene de fikk.

c. For aa representere alle vinnere i Lotto siste aar ville jeg bruke en liste. Siden det er bare navn som blir registrert, kan det holde at
vinnere i Lotto har samme navn, og da maa disse navn komme akkurat det antall ganger de blir tastet inn.

d. For aa representere all mat noen gjest i et selskap er allergisk mot ville jeg bruke en ordbok med en mengden inn i den. Her er det lurt aa
 bruke begge deler siden vi skal lagre navn paa gjesten og oversikten over mat han/hun er allergisk mot. Det er bedre aa bruke mengden her slik
 mat gjest er allergisk mot blir ikke gjentatt flere ganger.
"""
