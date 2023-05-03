import numpy as np
import matplotlib.pyplot as plt
import openpyxl
import pandas as pd
import random

zbior_danych = pd.read_csv('iris.data', header = None, names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])
print(zbior_danych)

data ={'sepal length':zbior_danych['sepal length'], 'sepal width':zbior_danych['sepal width'], 'c':np.random.randint(0, 150, 150), 'd':np.abs(zbior_danych['sepal length'] - zbior_danych['sepal width'])}
plt.scatter('sepal length', 'sepal width', c='c', s='d', data=data)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()