"""
Vi lager en funskjon som spor brukeren aa taste inn alderen. Deretter bruker den if-statement for aa
bestemme prisen paa biletten avhengig av alderen paa kjoperen og skriver den ut til brukeren.
"""
def bilettkjop():
    alder=int(input("Skriv inn alderen paa kjoperen: "))
    bilettpris=0

    if alder<=17:
        bilettpris=30
    elif alder>=63:
        bilettpris=35
    else:
        bilettpris=50

    print("Prisen er ", bilettpris)

bilettkjop()

"""
Jeg synes det var ikke noe galt med prosedyren paa den maaten jeg skrev den. Men hvis man skriver:

if alder<=17:
    bilettpris=30
elif alder>17:
    bilettpris=35
elif alder>=63:
    bilettpris=50

istedet for det jeg skrev, kommer man til aa faa problemer med alle brukerne som er over 63. Siden
programmet skal kjore linje etter linje, sjekker den forst om alder er mindre er lik 17. Hvis det er ikke sant,
da gaar den videre aa sjekke om alderen er storre enn 17. Siden 63 er storre enn 17, kommer programmet aa tenke at dette er sant
og kommer ikke til aa kjore den siste linje.
"""
