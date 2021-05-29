"""
Vi lager en tom liste og spor brukeren om aa taste inn et tall.
Vi skriver en while-lokke for aa legge alle tallene brukeren
skriver inn fram til brukeren oppgir tallet 0.
Vi bruker for-lokke for aa skrive ut alle tallene i listen.
Vi lager en varibel som er lik 0, og bruker for-lokke for aa
gaa gjennom listen og legge alle tallene sammen for aa faa summen,
og skriver summen ut.
Vi lager en variabel minst som vi setter, er lik nullte elementet
i listen. Vi bruker en for-lokke for aa gaa gjennom listen aa
sammenligne denne verdien med alle andre elementene i listen. Hvis
elementen er mindre enn den minst variablen, da setter vi det nye
elementet er lik minst og skriver variablen ut naar for-lokke har
gaatt gjennom alle elementene i listen.
Vi lager en variabel storst som vi setter, er lik nullte elementet
i listen. Vi bruker en for-lokke for aa gaa gjennom listen aa
sammenligne denne verdien med alle andre elementene i listen. Hvis
elementen er storre enn den storst variablen, da setter vi det nye
elementet er lik storst og skriver variablen ut naar for-lokke har
gaatt gjennom alle elementene i listen.
"""
liste=[]
tall=int(input("Tast inn et tall: "))
while tall!=0:
    liste.append(tall)
    tall=int(input("Tast inn et tall: "))

for element in liste:
    print(element)

minSum=0
for element in liste:
        minSum+=element
print("Summen av alle elementer er ", minSum)

minst=liste[0]
for e in liste:
    if e<minst:
        minst = e
print("Det minste elementet er ", minst)

storst=liste[0]
for i in range(1,len(liste)):
    if liste[i]>storst:
        storst=liste[i]

print("Det storste elementet er ", storst)
