a = eval(input("Wpisz liczbe a: "))
b = eval(input("Wpisz liczbe b: "))
c = eval(input("Wpisz liczbe c: "))

if a > 0 and a <= 10:
    print("Liczba a zawiera sie w przedziale (0, 10>")
    if a > b or b > c:
        if a > b and b > c:
            print("I jednoczesnie a > b and b > c")
        elif a > b:
            print("I jednoczesnie a > b")
        else:
            print("I jednoczesnie b > c")

else:
    print("Liczba a nie zawiera sie w przedziale od (0 do 10>")
    if a > b or b > c:
        if a > b and b > c:
            print("I jednoczesnie a > b and b > c")
        elif a > b:
            print("I jednoczesnie a > b")
        else:
            print("I jednoczesnie b > c")