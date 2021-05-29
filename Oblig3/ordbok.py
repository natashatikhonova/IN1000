"""
Forst lager vi en ordbok med navn paa varer i butikken og prisen paa hver enkel vare og skriver ut denne oversikten.
Programmet spor brukeren om aa oppgi 2 varer til med prisene paa dem. Naar brukeren gjor det, legger programmet disse
to verdiene inn i ordboken og skriver oppdaterte ordboken ut.
"""
butikk={"Melk ":14.90, "Brod ":24.90, "Yoghurt ":12.90, "Pizza ":39.90}
print(butikk)
varenavn1=input("Skriv inn et varenavn: ")
pris1=float(input("Hva koster den?"))
varenavn2=input("Skriv inn et til varenavn: ")
pris2=float(input("Hva koster den?"))
butikk[varenavn1]=pris1
butikk[varenavn2]=pris2
print(butikk)
