#Programmet sjekker om hvilken dato går først ila året
dato1=int(input("Skriv den første dato som et heltall. Skriv måned først og dag etterpå (Eksempel:905 for 5. september): "))
dato2=int(input("Skriv den andre dato som et heltall. Skriv måned først og dag etterpå (Eksempel:905 for 5. september): "))

#Programmet utfører if-statement for å se om to tall er lik, større eller midnre
if dato1<dato2:
    print("Riktig rekkefølge!")
elif dato1==dato2:
    print("Samme dato!")
else:
    print("Feil rekkefølge!")
