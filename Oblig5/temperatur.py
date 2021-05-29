"""
Forst lager jeg en funksjon som tar imot et filnavn og returnerer en ordbok.
Vi lager en tom ordbok og aapner filen.
Funksjonen gaar gjennom alle linjene i filen og legger dem til ordboken.

Deretter lager jeg en funksjon som tar inn en ordbok og et filnavn.
Vi aapner filen og bruekr for-lokke for aa gaa gjennom alle linjene
i ordboken og sammenligne temperaturen fra en fil med andre fil.
(bruker if-setning for det)
Hvis tallet er storre, da forandrer jeg verdien i ordboken.

Jeg lager en funksjon som tar imot en ordbok og et filnavn. Ved hjelp av
for-lokke gaar programmet gjennom alle linjene i ordboken og legger dem
til en fil.

Jeg lager en funksjon til som tar imot et filnavn og bruker for-lokke
for aa gaa gjennom alle linjene i filen.
Hvis temperaturen paa en av de dagene var storre enn 25, da legger vi til
en til teller-variabel(count). Hvis teller variabel er storre enn fem,
da skriver programmet ut start- og sluttdato paa bolgen. 


"""
def filTilOrdbok(filnavn):
    ordbok=dict()
    fil=open(filnavn, "r")
    for linje in fil:
        maaned=linje.split(",")
        ordbok[maaned[0]]=float(maaned[1])
    fil.close()
    return ordbok

print(filTilOrdbok("max_temperatures_per_month.csv"))

def hoyesteTemperatur(ordbok, filnavn):
    fil=open(filnavn, "r")
    for linje in fil:
        dato=linje.split(",")
        for element in ordbok:
            ordbok[element]=float(ordbok[element])
            dato[2]=float(dato[2])
            if element == dato[0] and dato[2]>ordbok[element]:
                print("Ny varmerekord paa", dato[1], dato[0],":", dato[2], "grader Celcius (gammel varmerekord var ", ordbok[element], "grader Celcius)")
                ordbok[element]=dato[2]
    fil.close()
    return ordbok

print(hoyesteTemperatur(filTilOrdbok("max_temperatures_per_month.csv"), "max_daily_temperature_2018.csv"))

def ordbokTilFil(ordbok, filnavn):
    fil=open(filnavn, "w")
    for linje in ordbok:
        skrivUt=linje+","+str(ordbok[linje])+"\n"
        fil.write(skrivUt)
    fil.close()

ordbokTilFil(hoyesteTemperatur(filTilOrdbok("max_temperatures_per_month.csv"), "max_daily_temperature_2018.csv"), "nyFil.csv")

def varmebolger(filnavn):
    ordbok=dict()
    fil=open(filnavn, "r")
    for linje in fil:
        dag=linje.split(",")
        ordbok[dag[0], dag[1]]= float(dag[2])
    count=0
    for linje in ordbok:
        if ordbok[linje]>25.0:
            count+=1
            if count==1:
                startdato=linje
        else:
            if count>=5:
                sluttdato=(int(linje[1])-1), linje[0]
                print("Varmebolge paa", count, "dager fra og med",startdato, "til og med",sluttdato)
                count=0
            else:
                count=0
    fil.close()
    return ordbok

varmebolger("max_daily_temperature_2018.csv")
