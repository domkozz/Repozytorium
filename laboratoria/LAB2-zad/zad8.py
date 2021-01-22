print("sprawdź czy trójkąt jest prostokątny")
a=float(input("podaj bok a: "))
b=float(input("podaj bok b: "))
c=float(input("podaj bok c: "))
if a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2:
    print("trójkąt jest prostokątny")
else:
    print("trójkąt nie jest")
