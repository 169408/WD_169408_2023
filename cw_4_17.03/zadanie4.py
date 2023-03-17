import numpy as np

def potegowanie(a, n):
    tablica = np.logspace(1, n, num=n, base=a, dtype='int64')
    return tablica

a = eval(input("Wpisz liczbe, ktora bedzie podstawa: "))
n = eval(input("Wpisz ilosc kolejnych poteg: "))

print(potegowanie(a, n))