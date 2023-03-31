import pandas as pd
import openpyxl
import numpy as np

# Zadanie 1
arkusz = pd.read_excel('datasets/imiona.xlsx')

print(arkusz)

# Zadanie 2

a = arkusz[arkusz['Liczba'] > 1000]
print(a)

b = arkusz[arkusz['Imie'] == "TOM"]
print(b)

c = arkusz['Liczba'].sum()
print(c)

d = arkusz.groupby(['Rok']).sum(['Liczba'])
print(d)

e = arkusz.loc[(arkusz['Rok'] >= 2000) & (arkusz['Rok'] <= 2005)]['Liczba'].sum()
print(e)
