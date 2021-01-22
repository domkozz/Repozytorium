import random
x=random.randint(1,100)
i=0
print("odgadnij liczbe z zakresu od 1 do 100, max 3 próby")
while i<3:
    a = int(input("podaj liczbe: "))
    if a>x:
        print("liczba za duza")
        i+=1
    elif a<x:
        print("liczba za mala")
        i+=1
    elif x==a:
        print("szukana liczba to",(x))
        print("brawo zgadłeś")
    if i==3:
        print("nie udalo ci sie, szukana liczba to",x,"xDDDD beka z cb")

input("\n\nAby zakończyć naciśnij enter")
