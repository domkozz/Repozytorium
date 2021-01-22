n = int(input("Podaj ile liczb chcesz wpisać: "))
b = 0
while True:
    a =int(input("Podaj liczbę:"))
    if a >= -6 and a <= 6:
        print("Podałeś liczbe z przedzialu ")
        b += 1
    if b == n:
        break
