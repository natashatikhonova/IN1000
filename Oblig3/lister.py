"""
Forst importerer vi math for aa kunne finne produktet senere. Vi lager en listen
og legger til et til tall til listen og skriver den ut.
Deretter lager vi en ny tom liste og spor brukeren im aa oppgi 4 navn og legger
disse navn til listen.
Programmet skal sjekke om listen inneholder mitt navn og skrive ut
en meldig avhengig av navn paa listen.
Vi finner en sum og produkt av tallene paa forste listen og legger dem til
den nye listen. Deretter legger vi to lister sammen og skriver den nye listen
ut.
Vi fjerner 2 siste elementene fra listen og skriver den oppdaterte listen ut.
"""
import math
array=[5,24,85]
array.append(14)
print(array[0], array[2])
ny_liste=[]
navn1=input("Oppgi forste navn: ").lower()
navn2=input("Oppgi andre navn: ").lower()
navn3=input("Oppgi tredje navn: ").lower()
navn4=input("Oppgi fjerde navn: ").lower()
ny_liste.extend((navn1, navn2, navn3, navn4))
mitt_navn="natasha"
if mitt_navn in ny_liste:
    print("Du husket meg!")
else:
    print("Har du glemt meg?")
total=sum(array)
produkt=math.prod(array)
ny_liste.extend((total,produkt))
dobbel_liste=array+ny_liste
print(dobbel_liste)
del dobbel_liste[-1]
del dobbel_liste[-1]
print(dobbel_liste)
