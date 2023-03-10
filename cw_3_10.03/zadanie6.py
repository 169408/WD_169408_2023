import random

punkty = 0
counter = 5

def guess_the_number(punkty, counter):
    random.seed()
    liczba = random.randint(0, 10)
    strzal = eval(input("Zgadnij liczbe od 1 do 10: "))
    while(strzal < 1 or strzal > 10):
        strzal = eval(input("Wpisz liczbe od 1 do 10: "))
    if(strzal == liczba):
        print("Wylosowana liczba to", liczba, ". Zdobywasz 10 punktów.")
        punkty += 10
    else:
        print("Wylosowana liczba to", liczba, ". Tracisz punkt.")
        punkty -= 1
    counter -= 1
    if(counter > 0):
        return guess_the_number(punkty, counter)
    return punkty

print("Koniec gry. Twoja punktacja to", guess_the_number(punkty, counter), "punktow.")