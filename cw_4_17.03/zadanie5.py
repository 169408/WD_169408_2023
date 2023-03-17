import numpy as np

def wek(n):
    tablica = np.arange(n, 0, -1)
    diagonal = np.diag([a for a in tablica], 0)
    return tablica, diagonal

dl = eval(input("Wpisz dlugosc wektora: "))
print(wek(dl)[0])
print(wek(dl)[1])
