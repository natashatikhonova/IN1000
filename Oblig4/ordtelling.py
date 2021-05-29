"""
Vi lager den forste funksjonen som tar imot et ord, og som
skal bruke for-lokke for aa gaa gjennom bokstavene i ordet og
telle hvor mange antall_bokstaver dette ordet inneholder, og
returnerer antallet av bokstaver i ordet.
Vi lager den andre fuksjonen som tar i mot en tekststreng og
bruker funksjon "split" for aa lage en liste med alle ordene
fra den tekststrengen. Vi ogsaa lager en tom ordbok.
Etter det bruker vi for-lokke for aa gaa gjennom alle elementene
(ordene) i listen (setningen) og legger denne elemnten til
ordboken og hvor mange ganger dette ordet ble bruk i tesktstrengen.
Deretter skriver vi ut hvor mange ord det er totalt i tekstrengen
ved bruk av aa sjekke lengde paa listen.
Siste skal vi lage en for-lokke som skal gaa gjennom alle elementene
i ordboken og skrive ut hvor mange ganger ordet ble brukt i setningen,
og bruke den forste funksjonen for aa skrive ut hvor mange antall_bokstaver
det er i hver av de ordene.
Saa skal vi spore brukeren om aa oppgi en setning som vi skal
bruke for aa kjore den andre funksjonen.
"""
def antall_bokstaver(ord):
    count=0
    for tegn in ord:
            count+=1
    return count

def antall_ord(setning):
    ordene=setning.split()
    teller=dict()

    for ord in ordene:
        if ord in teller:
            teller[ord]+=1
        else:
            teller[ord]=1
    print("Det er ",len(ordene),"ord i setningen din.")
    for i in teller:
        print("Ordet",i, "forekommer ", teller[i], "ganger, og har ", antall_bokstaver(i), "bokstaver")
    return teller

setning=input("Skriv en setning: ")
antall_ord(setning)
