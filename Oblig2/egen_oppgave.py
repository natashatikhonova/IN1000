"""
Lag et program som selger bussbiletter. Prisene er avhengig av alderen på kjøperen av biletten.
De som er mindre enn 6 aar faar lov aa ta buss gratis.
Barna til og med 12 maa kjope barnebilett for 30 kroner.
Ungdommer til og med 18 maa kjope ungdomsbilett for 40 kroner.
Alle andre maa kjope voksenbilett for 60 kroner.
MEN hvis man er student, faar man 25% rabatt. Dvs betaler 45 kroner.
Programmet maa spore brukeren om alderen og gi riktig pris avhengig av brukerens situasjonen. 
"""

def bilettSalg():
    alder=int(input("Hvor gammel er du?"))
    if alder<=6:
        print("Du faar gratis bilett!")
    elif alder<=12:
        print("Du trenger barnebilett! Det blir 30 kroner" )
    elif alder<=18:
        print("Du trenger ungdomsbilett! Det blir 40 kroner")
    else:
        print("Du trenger voksenbilett! Det blir 60 kroner")
        student=input("Er du student?").lower()
        if student=='ja':
            print("Du faar 25% rabatt! Det blir 45 kroner")
        else:
            print("Du faar dessverre ingen rabatt!")

bilettSalg()
