"""
Oppgave:
Lag et program hvor du kan lagre navn paa vennene dine, deres bursdager og telefonnummer.
Lag en tom ordbok og bruk en while-lokke for aa legge informasjon til den.
Bruk en for-lokke for aa skrive ut alle navn.
Spor brukeren om oppgi navn til vennen, og skriv ut informasjon du har lagret om han/henne.
"""
dict={}
svar="ja"
while svar=="ja":
    navn=input("Oppgi vennens navn: ")
    bursdag=input("Naar har han/hun bursdag? ")
    telefon=input("Oppgi hans/hennes telefonnummeret: ")
    dict[navn]={"Bursdag ": bursdag, "Telefonnummer ":telefon }
    svar=input("Vil du taste inn flere bursdager? ").lower()

print("Oversikt over vennene dine: ")
for x in dict:
    print(x)
name=input("Tast inn navn for aa faa informasjon om bursdagen: ")
print(dict[name])
