#hovedprogram som oppretter brettet

from spillebrett import Spillebrett

def main():
    #tar input fra brukeren om antall rader og kolonner i brettet
    inputRader=int(input("Hvor mange rader blir det?"))
    inputKolonner=int(input("Hvor mange kolonner blir det?"))

    #oppretter objektet og tegner brettet
    brett=Spillebrett(inputRader, inputKolonner)
    brett.tegnBrett()

    #spoer om input fra brukeren om aa fortsette spillet eller avslutte det
    nesteGenerasjon=''
    #hvis brukeren skriver inn 'q' avsluttes spillet
    while nesteGenerasjon!='q':
        #skriver ut hvilken generasjon spillet er paa og antall levende celler paa brettet
        print('Generasjon:',brett._generasjonsnummer, 'Antall levende celler:',brett.finnAntallLevende())
        #spoer brukeren om input
        nesteGenerasjon=input('Press enter for aa fortsette. Skriv inn q og trykk enter for aa avslutte:')

        #hvis brukeren vil fortsette, oppdateres brettet, og programmet skriver ut det oppdaterte brettet
        if nesteGenerasjon=='':
            brett.oppdatering()
            brett.tegnBrett()


main()
