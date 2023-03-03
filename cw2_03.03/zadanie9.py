x = input("Wpisz po jednej liczbie, zeby cod sie sconczyl napisz slowo end ")
list = []
while x != "end":
    if x.isdigit():
        list.append(x)
    print(list)
    x = input("Wpisz po jednej liczbie, zeby cod sie sconczyl napisz slowo end ")

print(list)
