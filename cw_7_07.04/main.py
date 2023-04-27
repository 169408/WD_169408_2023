import numpy as np
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

arkusz = pd.read_excel('datasets/imiona.xlsx')
print(arkusz)

# Zadanie 1

liczba = arkusz.groupby('Rok')['Liczba'].sum()
#print(liczba)
rok = arkusz['Rok'].unique()
#print(rok)

plt.plot(rok, liczba)
#plt.show()

# Zadanie 2

zd2 = arkusz.groupby('Plec')['Liczba'].sum()
#print(zd2)

zd2.plot.bar()
#plt.show()

# Zadanie 3

urodzony = arkusz.groupby(['Rok', 'Plec'])['Liczba'].sum().tail(10)
#print(urodzony)

urodzony.value_counts().plot(kind='pie', colors=['red', 'black'], title='Black - chlopaki, Red - dziewczyny')
#plt.show()

# Zadanie 4

zamowienia = pd.read_csv('datasets/zamowienia.csv', sep=';')
print(zamowienia)

sprzedawca = zamowienia.groupby('Sprzedawca')['idZamowienia'].count()
print(sprzedawca)

sprzedawca.plot.bar()
#plt.show()