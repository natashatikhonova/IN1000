#Programmet sjekker om hvilken dato kommer først ila året
#Programmet tar inn verdiene fra brukeren og gjør de til
#int(heltall)

dag1=int(input("Skriv den første dato. Først skriv en dag:"))
maned1=int(input("Na skriv en måned:"))
dag2=int(input("Skriv den andre dato. Først skriv en dag:"))
maned2=int(input("Nå skriv en måned:"))

#Programmet utfører if-statement for å teste hvilken dato
#kommer først
if  maned2>maned1:
    print("Riktig rekkefølge!")
elif maned1==maned2 and dag2>dag1:
    print("Riktig rekkefølge!")
elif dag1==dag2 and maned1==maned2:
    print("Samme dato!")
else:
    print("Feil rekkefølge!")
