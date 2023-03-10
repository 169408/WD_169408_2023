a1 = eval(input("Wpisz wartosc poczatkowa ciagu: "))
r = eval(input("Wpisz wielkosc o ile rosna kolejny elementy: "))
ilosc = eval(input("Wpisz ile elementow ma sumowac: "))

def sumaciagu(arg1 = 1, arg2 = 1, arg3 = 10):
    element = arg1
    suma = arg1
    for i in range(1, arg3):
        element += arg2
        suma += element

    return suma

print("Suma ", ilosc, " elementow ciaga arytmetycznego: ", sumaciagu(a1, r, ilosc))