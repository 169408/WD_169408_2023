print("Podane sa dwie proste rownaniami:\ny=a1x+b1\ny=a2x+b2")
a1 = eval(input("Wpisz wartosc a1: "))
a2 = eval(input("Wpisz wartosc a2: "))

def prostesa(arg1, arg2):
    if(arg1 == arg2):
        return "Dwie proste sa rownolegle"
    elif(arg1*arg2 == -1):
        return "Dwie proste sa prostopadle"

    return "Dwie proste nie sa ani rownolegle, ani prostopadle"

print(prostesa(a1, a2))
