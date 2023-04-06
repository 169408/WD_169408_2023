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

f = arkusz.groupby('Plec')['Liczba'].sum()
print(f)

sumimie = arkusz.groupby(['Plec', 'Imie']).sum(['Liczba'])
print(sumimie)

g1 = arkusz.loc[arkusz['Plec'] == 'M']
g2 = g1.groupby(['Plec', 'Imie']).sum(['Liczba'])
print(g1)
print(g2)


# Zadanie 3

zamowienia = pd.read_csv('datasets/zamowienia.csv', sep=';')
print(zamowienia)

zd1 = zamowienia['Sprzedawca'].unique()

print(zd1)
