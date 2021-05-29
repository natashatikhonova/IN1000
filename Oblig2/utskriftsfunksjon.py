'''
Programmet tar inn verdiene fra brukeren og lager dem i en funksjon.
Deretter skriver programmet ut tre ganger den informasjon den fikk
fra brukeren
'''
def hilsen():
    navn=input("Skriv inn navn: ")
    bosted=input("Hvor kommer du fra? ")
    print("Hei", navn, "! Du er fra ", bosted)

hilsen()
hilsen()
hilsen()
