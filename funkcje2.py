def wyswietl(arg1, arg2):
    print (f'Liczba1: (num1)')
    print (f'Liczba2: (num2)')

wyawietl(2, 4)

################ args ###################

def wyswietlArgs(num1, *args):
    print(f'Liczba 1: (num1)')
    for i in args:
        print(f'Następna wartość: (num1)')

wyswietlArgs(1, 2, 3, 4)

names = ['Anna', 'Julia', 'Tomasz']
wyswietlArgs(names)
wyswietlArgs(*names)

import os
os.system('cls')

