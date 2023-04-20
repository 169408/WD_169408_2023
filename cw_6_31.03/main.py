import pandas as pd
import openpyxl
import numpy as np

# Zadanie 1
arkusz = pd.read_excel('datasets/imiona.xlsx')

#print(arkusz)

# Zadanie 2

a = arkusz[arkusz['Liczba'] > 1000]
#print(a)

b = arkusz[arkusz['Imie'] == "TOM"]
#print(b)

c = arkusz['Liczba'].sum()
#print(c)

d = arkusz.groupby(['Rok']).sum(['Liczba'])
#print(d)

e = arkusz.loc[(arkusz['Rok'] >= 2000) & (arkusz['Rok'] <= 2005)]['Liczba'].sum()
#print(e)

f = arkusz.groupby('Plec')['Liczba'].sum()
#print(f)

sumimie = arkusz.groupby(['Plec', 'Imie'])['Liczba'].sum().reset_index()
#print(sumimie)

g = sumimie.loc[sumimie.groupby(by='Plec')['Liczba'].idxmax()]['Imie']
#print(g)

sumimie_zarok = arkusz.groupby(['Plec', 'Imie', 'Rok'])['Liczba'].sum().reset_index()
#print(sumimie_zarok)

h = sumimie_zarok.loc[sumimie_zarok.groupby(by=['Rok', 'Plec'])['Liczba'].idxmax()]
#print(h)

# Zadanie 3

zamowienia = pd.read_csv('datasets/zamowienia.csv', sep=';')
#print(zamowienia)

zd1 = zamowienia['Sprzedawca'].unique()
#print(zd1)

zam_sort = zamowienia.sort_values('Utarg', ascending=False)
zd2 = zam_sort['Utarg'].head(5)
#print(zd2)

zd3 = zamowienia.groupby('Sprzedawca')['Sprzedawca'].count()
#print(zd3)

zd4 = zamowienia.groupby('Kraj')['Utarg'].sum()
#print(zd4)

znrok = zamowienia[(zamowienia['Data zamowienia'] >= '2005-01-01') & (zamowienia['Data zamowienia'] <= '2005-12-31')]
zd5 = znrok[znrok['Kraj'] == 'Polska']['Utarg'].sum()
#print(zd5)

zd6 = zamowienia[(zamowienia['Data zamowienia'] >= '2004-01-01') & (zamowienia['Data zamowienia'] <= '2004-12-31')]['Utarg'].mean()
#print(zd6)

zd7_first = zamowienia[(zamowienia['Data zamowienia'] >= '2004-01-01') & (zamowienia['Data zamowienia'] <= '2004-12-31')]
zd7_first.to_csv('datasets/zamowienia_2004.csv', sep=';')
zd7_second = zamowienia[(zamowienia['Data zamowienia'] >= '2005-01-01') & (zamowienia['Data zamowienia'] <= '2005-12-31')]
zd7_second.to_csv('datasets/zamowienia_2005.csv', sep=';')
#print(zd7_first)
#print(zd7_second)