import numpy as np

def funk(n):
    tablica = np.arange(1, n*n)
    return tablica

n = eval(input("Wpisz liczbe: "))

print(funk(n))
print(funk(n).shape)