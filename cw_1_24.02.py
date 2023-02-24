# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# zadanie 1.
symbol = '*' * 19
print((symbol + "\n") * 4)

# zadanie 2
symbol = '*'
spacja = ' '
print((symbol * 19 + "\n") + (symbol + spacja * 17 + symbol + "\n") * 2 + (symbol * 19 + "\n"))

# zadanie 3
symbol = '*'
for i in range(1, 5):
    print(symbol*i)

# zadanie 4
print((512-282)/((47*48)+5))

# zadanie 5
x = 7
i = 1
while i < 6:
    print(x*i, end="")
    if i < 5:
        print('---', end="")
    i += 1

print('')

# zadanie 6
text = ""
text += "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. " \
        "przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, " \
        "pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, " \
        "a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
print(text)

# zadanie 7
a = eval(input("Wpisz jakas liczbe: "))
b = eval(input("Wpisz jakas liczbe: "))
print(a * b)

# zadanie 8
waga = eval(input("Wpisz jakas wage w kilo: "))
funt = waga*2.2
print("Waga w futach to: ", end="")
print(funt)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
