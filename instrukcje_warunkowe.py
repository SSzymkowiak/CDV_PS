#instrukcje warunkowe

x = 5
if x == 5:
    print("x jest równe 5")
    x = str(x)
    print("Wyświetlanie wartośći zmiennej x: " + x)
else:
    print("x jest różne od 5")
    print("Wyświetlanie wartości zmiennej x: ", x)

###################################

y = True
if y:
    print("Prawda")
else:
    print("Fałsz")

###################################

z = 5 > 6
if z:
    print("Prawda")
else:
    print("Fałsz")
print (z)

###################################

#j = "1"
#j = "0"

j = False

if bool(j):
    print("Prawda", j)
else:
    print("Fałsz", j)

########################################

if True:
    print("Prawda")
else:
    print("Fałsz")
