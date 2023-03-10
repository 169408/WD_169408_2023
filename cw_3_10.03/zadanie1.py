# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def monotonicznosc(arg):
    if (arg > 0):
        return "Funkcja jest monotoniczna rosnaca"
    elif (arg < 0):
        return "Funkcja jest monotoniczna malejaca"

    return "Funkcja jest stala"


print("Podana jest funkcja liniowa y = ax + b.")
a = eval(input("Wpisz wartosc a: "))
print(monotonicznosc(a))

