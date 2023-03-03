x = input("Wpisz kilka liczby po spacjach: ")
lista = x.split(" ")
rozmiar = len(lista)

for i in range(0, rozmiar, 1):
    print(lista[i], "^ 2 = ", int(lista[i]) * int(lista[i]))


