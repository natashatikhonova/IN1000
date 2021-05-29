'''
Programmet tar inn temperatur i fahrenheit fra brukeren og skriver den ut.
Deretter konverterer programmet det temperaturet fra brukeren til celsius,
avrunder den til 2 desimaltall og skriver den ut.
'''
fahrenheit=int(input("Skriv inn temperatur i fahrenheit: "))
print(fahrenheit)
celsius=round((fahrenheit-32)*5/9, 2)
print(celsius)
