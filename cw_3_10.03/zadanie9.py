wysokosc = eval(input("Podaj wysokosc diamentu nie mniej jak 3: "))
while(wysokosc < 3):
    wysokosc = eval(input("Podaj wysokosc diamentu nie mniej jak 3: "))

def litera(arg):
    s = arg-1
    n = 1
    if(arg % 2 == 0):
        arg -= 1
    for i in range(0, arg):
        if(i == 0):
            print(" " * s + "*" + " " * s)
            s -= 1
        elif(i < int(arg/2)):
            print(" " * s + "*" + " "*n + "*" + " " * s)
            n += 2
            s -= 1
        elif(i == int(arg/2)):
            print(" "*s + "*" * arg + " "*s)
            n += 2
            s -= 1
        else:
            print(" "*s + "*" + " " * n + "*" + " "*s)
            n += 2
            s -= 1
    return 0

litera(int(wysokosc))