import numpy as np
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

arkusz = pd.read_excel('datasets/imiona.xlsx')
print(arkusz)

liczba = arkusz.groupby('Rok')['Liczba'].sum()
print(liczba)
rok = arkusz['Rok'].unique()
print(rok)

plt.plot(rok, liczba)
plt.show()