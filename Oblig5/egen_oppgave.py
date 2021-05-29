"""
Jeg folgte forslaget fra oppgaven.

Forst lager jeg en funksjon som tar imot et filnavn og returnerer en ordbok.
Vi lager en tom ordbok og aapner filen.
Funksjonen gaar gjennom alle linjene i filen og legger dem til ordboken.
Vi bruker funksjonen fra oppgaven en for aa skrive ut maalene i centimeter.

Deretter skriver jeg en main prosedyr hvor jeg lager en variabel ordbok
som kjorer funksjonen filTilOrdbok med en fil-argument.
Jeg bruker en for-lokke for aa gaa gjennom alle linjene i ordboken
og koventerer tommer til centimeter; paa slutten skriver jeg ut
de nye maalingene i centimeter.
"""

def filTilOrdbok(filnavn):
    ordbok=dict()
    fil=open(filnavn, "r")
    for linje in fil:
        maalet=linje.split(":")
        ordbok[maalet[0]]=float(maalet[1])
    fil.close()
    return ordbok

def tommerTilCm(antallTommer):
    assert antallTommer>0
    return antallTommer*2.54

def main():
    ordbok=filTilOrdbok("text.csv")

    for linje in ordbok:
        ny_verdi=tommerTilCm(float(ordbok[linje]))
        ordbok[linje]=ny_verdi

    print("Maalene i centimeter: \n",ordbok)

main()
