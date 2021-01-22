import random

x = int(input("Podaj górny próg"))

z = int(input("podaj dolny próg"))

n = int(input("podaj ilość"))

i = 0

tab = []

while i != n:

    liczba = random.randint(z,x)

    tab.append(liczba)

    i += 1

print(tab)

print(tab [n-3])

k = int(input("Podaj element do usunięcia"))

tab.pop(k-1) ##Bo jak użytkownik wpisze 1 to mu usunie widzialny element 2 i się będzie denerwował :)

print(tab)



y = int(input("Podaj górny próg"))

t = int(input("podaj dolny próg"))

u = int(input("podaj ilość"))

p = 0

tab2 = []

while p != u:

    liczba2 = random.randint(t,y)

    tab2.append(liczba2)

    p += 1

print(tab2)

tab3 = tab + tab2

print(tab3)

output = []

for x in tab3:

    if x not in output:

        output.append(x)

print(output)

for x in output:

    l = tab3.count(x)

    print("liczby", x,"było", l)