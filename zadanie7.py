import pandas as pd
import numpy as np

def zad7(n):
    mat = np.zeros((n, n))
    for i in range(1, n+1):
        mat += np.diag(np.full(n-i+1, i*2), i-1)
        if(i > 1):
            mat += np.diag(np.full(n-i+1, i*2), -(i-1))
    print(mat)


zad7(4)
