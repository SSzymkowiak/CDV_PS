#precyzja

x = "(0: .f)".format(5)
print(x)

def plnToCHF(value):
    kursCHF = 3.7536
    print(f'\nId franka wewnątrz funkcji: (id(kursCHF))')
    print(f'\nKurs franka: (kursCHF)')
    iloscCHF = value /kursCHF
    iloscCHF = "{0:.0f}" .format(iloscCHF)
    return iloscCHF


def pltoUSD(value):
    kursUSD = 3.4567
    print(f'\nId dolara wewnątrz funkcji: (id(kursUSD))')
    print(f'\nKurs dolara: (kursUSD)')
    iloscUSD = value /kursUSD
    iloscUSD = "{0:.0f}" .format(iloscUSD)
    return iloscUSD

print(kursUSD)
print(id(kursUSD))
print(plntoUSD(100))

zmiennaGlobal = 10
print(f'\nWartość zmiennej globalnej wewnątrz funkcji: {zmiennaGlobal}')
print(f'\nId zmiennej globalnej wewnątrz funkcji: (id(zmiennaGlobal))')

def spr():
    zmiennaGlobal = 20
    print(f'\nWartość miennej globalnej: (zmiennaGlobal)')
    print(f'\nId zmiennej globalnej wewnątrz funkcji: (id(zmiennaGlobal)'),
