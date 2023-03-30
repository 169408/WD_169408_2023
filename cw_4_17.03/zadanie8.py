import numpy as np

def foo8(tablica, h=1):
    if(h == 1):
        pol = int(n/2)
        return tablica[0:pol,:]
    pol = int(k/2)
    return tablica[:,0:pol]

n = eval(input("Wpisz ilosc wierszy: "))
k = eval(input("Wpisz ilosc kolumn: "))
kierunek = eval(input("Wpisz kierunek po jakim podzielic macierz, 1 - poziomie, 2 - pionie: "))

macierz = np.ones((n, k))
for i in range(n):
    macierz[i] = i+1

print(macierz, "\n\n")

if(kierunek == 2):
    if (k % 2 != 0):
        print("Nie mozliwe podzielic macierz na pol w pionie")
    else:
        print(foo8(macierz, kierunek))
else:
    if (n % 2 != 0):
        print("Nie mozliwe podzielic macierz na pol w poziomie")
    else:
        print(foo8(macierz, kierunek))