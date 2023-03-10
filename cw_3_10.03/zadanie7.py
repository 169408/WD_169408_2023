liczba = eval(input("Wpisz jakas liczbe calkowita: "))

def digital_r(arg1):
    suma = 0
    while(arg1 > 0):
        suma += int(arg1 % 10)
        arg1 = int(arg1 / 10)
    if(suma < 10):
        return int(suma)

    return digital_r(suma)

print("Suma cyfr liczby", liczba, "to", digital_r(liczba))