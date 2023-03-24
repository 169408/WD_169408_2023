import numpy as np

def macierz(n):
    tablica = np.ones((n, n))
    max = 2*n + 1
    #tablica[:, ::-1] = np.fromiter(range(2, max, 2), dtype='int32')
    #tablica[::-1,:] = np.fromiter(range(2, max, 2), dtype='int32')
    np.fill_diagonal(tablica, 2)
    #tablica[:,0] = np.fromiter(range(2, max, 2), dtype='int32')
    #tablica[0,:] = np.fromiter(range(2, max, 2), dtype='int32')
    #tablica[n-1,::-1] = np.fromiter(range(2, max, 2), dtype='int32')
    #tablica[::-1, n-1] = np.fromiter(range(2, max, 2), dtype='int32')
    return tablica


a=np.arange(1, 7, 2)

z=np.fromiter(range(5),dtype='int32')
print(macierz(5))