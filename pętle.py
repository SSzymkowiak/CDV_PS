#while
licznik = 0
while (licznik < 3):
    licznik = licznik + 1
    print("CDV")
print(licznik)

############################

licznik = 0
while (licznik < 3):
    licznik += 1
    print(licznik, end="")
else:
    print("Koniec pętli")

##############################
##########   FOR

lista = ["Jan","Anna","Paweł"]

for i in lista:
    print(i)

##############################

text = "Janusz"
for i in text:
    print(i)

##############################

slownik = dict()
slownik['a'] = 1
slownik ['b'] = 2

for i in slownik:
    print("%s %d"%(i, slownik[i]))

##################################

lista = ["Kebab","Hotdog","Falafel"]
for index in range(len(lista)):
    print(lista[index])
