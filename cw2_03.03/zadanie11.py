wysokosc = eval(input("Podaj wysokosc diamentu nie mniej jak 3 i nie wiecej jak 9: "))
n = 1
if wysokosc in range(3, 10):
    if wysokosc % 2 == 0:
        wysokosc = wysokosc - 1
    glowny = int((wysokosc+1) / 2)
    s = glowny
    for i in range(1, wysokosc+1):
        if i == glowny:
            print("o"*wysokosc)
        else:
            if i > glowny:
                n -= 2
                print((" " * s) + ("o" * n) + (" " * s))
                s += 1
            else:
                s -= 1
                print((" " * s) + ("o" * n) + (" " * s))
                n += 2