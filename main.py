import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl
import numpy as np

def zad1():
    df = pd.read_excel('docs/imiona.xlsx')

    df_od_k = df[df['Imie'].str[0] == 'K']
    imiona = df_od_k['Imie'].unique()
    print(len(imiona))

#zad1()

def zad2():
    df = pd.read_excel('docs/imiona.xlsx')

    dataf = df.groupby(['Plec', 'Imie'])['Liczba'].sum().reset_index()
    k = dataf[dataf['Plec'] == 'K'].reset_index()
    k_max = k['Liczba'].idxmax()
    k_imie = k.iloc[k_max]['Imie']
    m = dataf[dataf['Plec'] == 'M'].reset_index()
    m_max = m['Liczba'].idxmax()
    m_imie = m.iloc[m_max]['Imie']
    print("najczesciej nadawane imie zenskie", k_imie)
    print("najczesciej nadawane imie meskie", m_imie)

zad2()

def zad3():
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 6))
    fig.suptitle('Liczba narodzonych dzieci w latach 2010-2015')
    df = pd.read_excel('docs/imiona.xlsx')

    ax1.set_title("Wykres w pandasie")
    ax2.set_title("Wykres w seabornie")
    #df['Rok'] = df['Rok'].astype('int64')
    dzieci = df[(df['Rok'] >= 2010) & (df['Rok'] <= 2015)]
    data_plec = dzieci.groupby('Plec')['Liczba'].sum()
    data_plec.plot.bar(ax=ax1)
    ax1.legend()
    sns.barplot(data=dzieci, x='Plec', y='Liczba', estimator=sum, errorbar=None, ax=ax2)
    plt.show()

zad3()