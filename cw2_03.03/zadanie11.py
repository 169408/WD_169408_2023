wysokosc = eval(input("Podaj wysokosc diamentu nie mniej jak 3 i nie wiecej jak 9: "))

if wysokosc in range(3, 10):
    if wysokosc % 2 == 0:
        wysokosc = wysokosc - 1
    for i in range(1, wysokosc+1):
        if i % 2 == 0:
            print("ooo")
        else:
            print(" o ", sep=None)
