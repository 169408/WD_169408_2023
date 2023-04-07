import numpy as np

def zad8(tab, k='poziomo'):
    if k == 'piomowo':
        if (tab.shape[0] % 2 != 0):
            print("Tablica posiada nieparzysta liczbe wierszy")
            return
        else:
            mat1 = tab[:int(tab.shape[0] / 2)]
            print(mat1)
    if k == 'poziomo':
        if(tab.shape[0] % 2 != 0):
            print("Tablica posiada nieparzysta liczbe wierszy")
            return
        else:
            mat1 = tab[:, int(tab.shape[0]/2)]
            mat2 = tab[:, int(tab.shape[0]/2):]
            print(mat1)

uneval = np.arange(9).reshape(3, 3)
mat_eval = np.arange(16).reshape(4, 4)

zad8(uneval)
zad8(mat_eval)