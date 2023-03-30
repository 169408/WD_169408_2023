import numpy as np

def macierz(n):
    tablica = np.ones(n, dtype=int)*2
    matr = np.diag(tablica)

    for i in range(1, n):
        tablica2 = np.ones(n-i, dtype=int)*2*(i+1)
        matr += np.diag(tablica2, i) + np.diag(tablica2, -i)
    return matr

n = eval(input("Wpisz wymiar macierzy: "))
print(macierz(n))



