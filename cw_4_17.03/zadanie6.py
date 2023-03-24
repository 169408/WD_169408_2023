import numpy as np

tablica = np.empty((6, 6), dtype="U1")

def foo6():
    words = ['malina', 'jagoda', 'lizak']
    slowo1 = 'malina'
    slowo2 = 'lizak'
    slowo3 = 'jagoda'
    slowo3_1 = slowo3[::-1]
    print(slowo3_1)

    macierz = np.zeros((6, 6), dtype=str)
    np.fill_diagonal(macierz, list(slowo2))
    macierz[:,0] = np.fromiter(slowo1, dtype='S1')
    macierz[5:,::-1] = np.fromiter(slowo3, dtype='S1')
    return macierz

print(foo6())