"""
Vi lager en tom liste og bruker en for-lokke for aa spore brukeren
aa taste inn et reisemaal. For-lokke kommer til aa spore
brukeren 5 ganger og legge svaret til listen.
Deretter lager vi to tome lister til og bruker for-lokker for aa
ta imot verdiene fra brukeren og legge dem til listene.
Naar vi er ferdig med de tre listene, lager vi en ny liste som
bestaar av de tre gamle listene.
Vi bruker for-lokke for aa gaa gjennom alle elementene i den nye
listen og printer dem ut.
Vi lager en gyldig boolean-variabel som vi skal bruke for aa
sjekke om inputen til bruker var gyldig eller ikke.
Vi bruker en while-lokke som kommer til aa spore brukeren
om aa oppgi to indekser og bruke if-statement for aa sjekke
om de to indeksene er gyldige posisjonene i den nye listen "reiseplan".
Hvis brukerens input var gyldig, da skriver vi ut det elementet
som er plassert paa denne posisjonen som brukeren har oppgitt,
og setter gyldig-variabel lik True slik lokke stoppes. Hvis
posisjonen er ugyldig, skriver programmet ut en feilmelding og
spor om aa oppgi en ny posisjon. 
"""
steder=[]
for e in range(5):
    steder.append(input("Tast inn et reisemaal: "))

klesplagg=[]
for e in range(5):
    klesplagg.append(input("Tast inn klesplagg: "))

avreisedatoer=[]
for e in range(5):
    avreisedatoer.append(input("Tast inn avreisedato: "))
reiseplan=[steder,klesplagg,avreisedatoer]

for e in reiseplan:
    print(e)

gyldig=False

while (gyldig!=True):
    i1=int(input("Oppgi forste indeks: "))
    i2=int(input("Oppgi andre indeks: "))

    if(i1<=(len(reiseplan)-1) and i1>=0 and i2<=(len(reiseplan[i1])-1) and i2>=0):
        print(reiseplan[i1][i2])
        gyldig=True
    else:
        print("Ugyldig input!")
