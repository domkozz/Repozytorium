tup1 =[]
tup2 =[]
a = (input("Podaj 1 słowo: "))
b = (input("Podaj 1 słowo: "))

tup1 = ''.join(sorted(a))
print(a)
tup2 = ''.join(sorted(b))
print(b)
if tup1 == tup2:
    print("Słowa są anagramami")
else:
    print("Słowa są nie anagramami")
