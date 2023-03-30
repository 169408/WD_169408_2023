import numpy as np

def fibo(n):
    if(n == 0):
        return 0
    if(n == 1 or n == 2):
        return 1
    return fibo(n-1)+fibo(n-2)

macierz = np.array([], dtype=int)
for i in range(0, 25):
    macierz = np.append(macierz, fibo(i))

new = np.reshape(macierz, (5, 5))

print(new)