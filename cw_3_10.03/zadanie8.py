import random

questions = 1
wrong = 0
correct = 0

def multipli_game(arg1, arg2, arg3):
    random.seed()
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    while(arg1 <= 10):
        print("Pytanie", arg1, ":", a, "x", b, "= ", end="")
        answer = eval(input())
        if(answer == a*b):
            print("Poprawna odpowiedz!")
            arg3 += 1
        else:
            print("Bledna odpowiedz, poprawna odpowiedz jest", a*b)
            arg2 += 1
        return multipli_game(arg1+1, arg2, arg3)
    return arg2, arg3

result = multipli_game(questions, wrong, correct)

print("Koniec gry!\nBledne odpowiedzi:", result[0], "\nPoprawne odpowiedzi:", result[1])