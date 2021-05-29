"""
Jeg lager en tom ordbok.
Deretter lager jeg en funksjon som tar imot et navn og ordboken, splitter navnet, lager
et brukernavn fra navnet og returnerer det brukernavnet.
Funksjonen altså sjekker om brukernavnet eksisterer fra for. Jeg bruker if-setning
for aa se om dette brukernavnet finnes i ordboken. Hvis den finnes, da skal jeg legge
en bokstav til brukernavnet.
Jeg lager en funksjon som tar imot et brukernavn og et suffix.Funksjonen
legger de sammen og returnerer en epost.
Jeg lager en funksjon som gaar gjennom alle elementene i ordboken og
srkiver ut alle epostene.
Jeg tar input fra brukeren og gaar inn i en while-lokke:
1. naar bruker taster inn "i", da tar programmet 2 inputer fra brukeren
(navn og epost suffix) og kaller paa lagEpost funksjon med disse
to argumentene. Programmet spor om inputen igjen.
2. naar bruker taster inn "p", da skriver programmet ut alle epostene som
ligger inn i ordboken og spor om inputen igjen
3. naar bruker taster inn "s", da avsluttes programmet med break.

"""
eposter=dict()
def lagBrukernavn(navn, ordbok):
    list=navn.lower().split()
    i=1
    brukernavn=list[0]+list[1][:i]
    finnes=True
    while finnes:
        if brukernavn in ordbok:
            i+=1
            brukernavn=list[0]+list[1][:i]
        else:
            finnes=False

    return brukernavn

def lagEpost(brukernavn, suffix):
    epost=str(brukernavn)+"@"+str(suffix)
    return epost

def printEposter(ordbok):
    for element in ordbok:
        print(lagEpost(element, ordbok[element]))

printEposter({"olan": "ifi.uio.no",
"karian": "student.matnat.uio.no"})

bruker=str(input("Tast inn streng (i for aa lage ny brukernavn; p for aa skrive ut alle brukernavn; s for aa avslutte programmet): "))
while bruker=="i":
    navn=str(input("Tast inn et navn: "))
    epost=str(input("Tast inn epost suffix: "))
    brukernavn=lagBrukernavn(navn, eposter)
    eposter[brukernavn]=epost
    bruker=str(input("Tast inn streng: "))
    while bruker=="p":
        printEposter(eposter)
        bruker=str(input("Tast inn streng: "))
        while bruker=="s":
            print("Programmet er avsluttet!")
            break
