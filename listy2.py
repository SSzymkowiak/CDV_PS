#listy
programowanie = ["PHP", "Python", "Java"]
print(type(programowanie))
programowanie.append("C#")
programowanie.append("PHP")
print(programowanie)
ile = programowanie.count("PHP")
print("Ile: ", ile)

#tuple

imiona = ("Julia","Anna","Tomek")
print(type(imiona))
print(imiona[0])


#słownik
osoba = {"imie":"Julia","nazwisko":"Nowak","wiek":20}
print(osoba)
print(type(osoba))

#print(osoba[0])   #błąd
print(ososba["imie"])
print(osoba.keys())
print(osoba.get("wzrost", NULL))
print(osobs.get("naziwsko", NULL))
#