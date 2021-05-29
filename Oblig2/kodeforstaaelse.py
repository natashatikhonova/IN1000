"""
1. Dette er ikke lovlig kode. Et tall og en string kan ikke skrives ut samtidig.
For å gjøre det må man konvertere int til en string.
2. Programmet kunne ikke kjøres fordi b er int og ikke string.
Det blir en feil ved å forsøke å kjøre denne koden.
"""
a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
print (b + "Hei!")
