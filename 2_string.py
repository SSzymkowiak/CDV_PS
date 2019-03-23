tekst = "Anna, paweł, Tomek"

tab = tekst.split(" , ")

print(tekst)
print(tab)

imie1 = tab[0]
print(imie1)

print("Twoje imie: " + imie1)

imieDuze = imie1.upper()
print(imieDuze)

imieMale = imie1.lower()
print(imieMale)

#sprawdzanie zawartości
zawartosc = imie1.isalpha()
print(zawartosc)
print(type(zawartosc))

imie = ""
zawartosc = imie.isalpha()
print(zawartosc)
print(type(zawartosc))

imie = "Julia"
print("\mDane użytkownika\nMasz na imię: " + imie)

text1 = "Jan\n"
text2 = "Nowak"
print(text1 + text2)
print(text1 + " " + text2)

#Wyświetlanie  łańcuchów znaków

#Wszystkie wersje Pythona

#nowsze wersje Pythona 2.6 i >3

#help(text.replace)

#new = text.replace("PHP", "C#")
#print(new)

#wypisywanie danych
rok = "2013"
miesiac = "marzec"
dzien = "23"

print("Data: " , end="")
print(dzien, miesiac, rok)

