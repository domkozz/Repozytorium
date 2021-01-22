[13:39] Tomasz 43170
suma = 0
i = 1
x = int(input("Podaj liczbę: "))
while i < x:
    if x % i == 0:
        suma += i
    i += 1
if suma == x: print(x," to liczba doskonała")
else: print(x," nie jest liczbą doskonałą")

