pytania = [
    "1.Co definiuje się słowem def?\n(a)listy\n(b)słowniki\n(c)funkcje\n\n",
    "2.Co robi print?\n(a)Kończy pętle\n(b)Oblicza równanie\n(c)Wyświetla tekst\n\n",
    "3.Co robi funkcja len()?\n(a)Tworzy listę len\n(b)Zwraca ilość elementów listy\n(c)Podaje współczynnik zmienności\n\n",
    "4.Jaka jest domyślna wartość input'a?\n(a)str\n(b)int\n(c)float\n\n",
    "5.Jaką wartość da 2%2?\n(a)1\n(b)0\n(c)2\n\n",
    "6.Funkcja while jest stosowana do:\n(a)Tworzenia pętli\n(b)Tworzenia ciągów plików\n(c)Tworzenia zaprzeczenia\n\n",
    "7.Funkcja sqrt(x) zwraca:\n(a)Pierwiastek kwadratowy z x\n(b)Pierwiastek trzeciego stopnia z x\n\n",
    "8.lower():\n(a)zmienia wszystkie duże litery na małe\n(b)zmienia pierwszą dużą literę na małą\n\n",
    "9.Słownik tworzy się za pomocą:\n(a)[]\n(b)()\n(c){}\n\n",
    "10.Krotkę można edytować w trakcie pracy.\n(a)Prawda\n(b)Fałsz\n\n"]


abc= ["c", "c", "b", "a", "b", "a", "a", "a", "c", "b"]#poprawne odpowiedzi

x=0#pojemnik na punkty
def wynik(punkty):
    if punkty<3:
        print("\nTwoja ocena to niedostateczny/",1)
    elif punkty>=3 and punkty<5:
        print("\nTwoja ocena to dwa/",2)
    elif punkty>=5 and punkty<=7:
        print("\nTwoja ocena to dostateczny/",3)
    elif punkty>7 and punkty<=9:
        print("\nTwoja ocena to dobry/",4)
    elif punkty>9:
        print("\nTwoja ocena to 5/",4)
    return(" ")

print(pytania[0])
answer=input("Podaj odpowiedź: ")
if answer==abc[0]:
    x+=1
print(pytania[1])
answer=input("Podaj odpowiedź: ")
if answer==abc[1]:
    x+=1
print(pytania[2])
answer=input("Podaj odpowiedź: ")
if answer==abc[2]:
    x+=1
print(pytania[3])
answer=input("Podaj odpowiedź: ")
if answer==abc[3]:
    x+=1
print(pytania[4])
answer=input("Podaj odpowiedź: ")
if answer==abc[4]:
    x+=1
print(pytania[5])
answer=input("Podaj odpowiedź: ")
if answer==abc[5]:
    x+=1
print(pytania[6])
answer=input("Podaj odpowiedź: ")
if answer==abc[6]:
    x+=1
print(pytania[7])
answer=input("Podaj odpowiedź: ")
if answer==abc[7]:
    x+=1
print(pytania[8])
answer=input("Podaj odpowiedź: ")
if answer==abc[8]:
    x+=1
print(pytania[9])
answer=input("Podaj odpowiedź: ")
if answer==abc[9]:
    x+=1
print("\nIlość zdobytych przez ciebie punktów to:",x,wynik(x))
input("\nAby zakończyć naciśnij enter")


