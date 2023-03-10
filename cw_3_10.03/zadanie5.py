lista = ["Hello", "World", "I am computer", "Geek"]

# punkt a

def dodaj_znak(lista):
    for i in range(0, len(lista)):
        lista[i] = lista[i].replace(lista[i], lista[i]+"!")
    return lista

print("Lista: ", dodaj_znak(lista))

# punkt b

lista = ["Hello", "World", "I am computer", "Geek"]

def dodajZnak(lista):
    lista2 = []
    for i in range(0, len(lista)):
        lista2.append(lista[i] + "!")
    return lista2

print("Lista: ", dodajZnak(lista))