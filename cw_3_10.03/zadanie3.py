import math

print("Wpisz stony trojkata prostokatnego: ")
a = eval(input("Wpisz strone a: "))
b = eval(input("Wpisz strone b: "))

def przeciwprostokatna(arg1 = 3, arg2 = 4):
    c = math.sqrt(arg1*arg1 + arg2*arg2)
    return c

print("dlugosc przeciwprostokatnej: ", przeciwprostokatna(a, b))