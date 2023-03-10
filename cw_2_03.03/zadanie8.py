i = eval(input("Wpisz liczbe wielocyfrowa: "))
sum = 0

for x in str(i):
    sum += int(x)

print(sum)