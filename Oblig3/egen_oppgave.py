"""
Lag en funksjon hvor du lager en ordbok som har oversikt over de tre emnene paa forste semester pa ProSa
(IN1000,IN1020 og Exphil). Hver emne skal inneholde oversikt over obligene i lopet av semester og hvor mange poeng en
student fikk, om obligen ble ikke levert eller oppgaven er ikke tilgjengelig. Deretter skal du skrive ut navn paa
alle emnene og spor bruker om oppgi en emne.
Bruk if-statement for aa skrive ut oversikten over alle obligene.
Hvis emne er ikke i listen, skriv ut en feilmelding. 
"""
def obliger():
    innleveringer={
    "IN1000":{
    "Oblig 1":"3/3 poeng!",
    "Oblig 2":"3/3 poeng!",
    "Oblig 3":"2/3 poeng!",
    "Oblig 4":"Ikke levert!",
    "Oblig 5":"3/3 poeng!",
    "Oblig 6":"Ikke levert!",
    "Oblig 7":"Husk aa levere oppgaven!"
    },

    "IN1020":{
    "Oblig 1":"Bestaatt!",
    "Oblig 2":"Ikke levert!",
    "Oblig 3":"Oppgaven er ikke tilgjengelig!"
    },
    "EXPHIL":{
    "Oblig 1":"Bestaat!",
    "Oblig 2":"Ikke levert!"
    }
    }
    print(innleveringer.keys())

    fag=input("Tast inn emne for aa se alle obligene: ").upper()
    if fag in innleveringer:
        print(innleveringer[fag])
    else:
        print("Dette faget er ikke registert!")


obliger()
