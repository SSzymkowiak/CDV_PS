programowanie = ["Python", "C#", "JS", "PHP", "Java"]

print(programowanie)
print(type(programowanie))

pierwszy = programowanie[0]
print("Pierwszy język programowania: " + pierwszy)

trzyElementy = programowanie[0:3]
print(trzyElementy)

ostatni = programowanie[-1]
print(ostatni)

#Dodawanie nowego elementu na końcu listy
programowanie.append("R")
print(programowanie)

#Zliczanie elementów w liście
programowanie.append("Python")
ile = programowanie.count("Python")
print(ile)

iloscElementow = len(programowanie)
#print("Ilość elementów w liście: ", iloscElementow)
print("Ilość elemnetów w liście: ", end="")
print(iloscElementow)

#Połączenie list
print("\n",programowanie)
inneJezyki = ["C","C++","Pascal"]
print("Połączenie list")
programowanie.extend(inneJezyki)
print(programowanie)
print(inneJezyki)

#Wyczyszczenie listy
nowa = programowanie
print("Lista nowa: ",end="")
print(nowa)

#nowa.clear()
print("Lista programowanie: ",end="")
print(programowanie)
print("Lista nowa: ",end="")
print(nowa)

