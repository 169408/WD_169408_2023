import numpy as np
import matplotlib.pyplot as plt
import openpyxl
import pandas as pd

arkusz = pd.read_excel('imiona.xlsx')

wsl1 = arkusz.groupby('Plec')['Liczba'].sum()

plt.subplot(1, 3, 1)
wsl1.plot.bar('K', 'M', color=['red', 'blue'])
plt.ylabel('ilosc')

meszczyzny = arkusz[arkusz['Plec'] == 'M'].groupby(['Rok'])['Liczba'].sum()
kobiety = arkusz[arkusz['Plec'] == 'K'].groupby(['Rok'])['Liczba'].sum()
rok = arkusz['Rok'].unique()

plt.subplot(1, 3, 2)
plt.plot(rok, meszczyzny, label='Meszczyzny')
plt.plot(rok, kobiety, label='Kobiety')
plt.xlabel('rok')
plt.ylabel('M lub K')
plt.legend(loc=1)

wsl2 = arkusz.groupby('Rok')['Liczba'].sum()

plt.subplot(1, 3, 3)
wsl2.plot.bar()
plt.xlabel('rok')
plt.ylabel('Liczba')
plt.show()

