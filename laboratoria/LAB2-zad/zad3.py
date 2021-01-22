a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))
c = int(input("Podaj liczbe c: "))
if a > b and a > c:
    print("a jest największe")
if a > b and a == c:
    print("a i c są takie same i większe od b")
if a > c and a == b:
    print("a i b są takie same i większe od c")
if b > a and b > c :
    print("b jest największe")
if b > a and b == c:
    print("b i c są takie same i większe od a")
if c > a and c > b:
    print("c jest największe")
if a==b and a==c:
    print("wszystkie liczby są takie same")