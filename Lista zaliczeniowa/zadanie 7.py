import datetime

def wielkanoc():
    print("Obliczymy kiedy będzie wielkanoc w wybranym przez ciebie roku.")
    y=int(input("Podaj rok: "))
    a=y%19
    b=int(y/100)
    c=y%100
    d=int(b/4)
    e=b%4
    f=int((b+8)/25)
    g=int((b-f+1)/3)
    h=(19*a+b-d-g+15)%30
    i=int(c/4)
    k=c%4
    l=(32+2*e+2*i-h-k)%7
    m=int((a+11*h+22*l)/451)
    p=(h+l-7*m+114)%31
    p=(p+1)
    n=int((h+l-7*m+114)/31)
    print("Wielkanoc w roku:",y,"wypada w dniu:",p,", miesiąca:",n)
    return (" ")

today = datetime.date.today()
print('Dziś jest:', today)

yesterday = today - datetime.timedelta(days=1)
print('Wczoraj był:', yesterday)

tomorrow = today + datetime.timedelta(days=1)
print('Jutro będzie:', tomorrow)
print("Określmy w którym dniu tygodnia się urodziłeś.")
rok=int(input("Podaj rok swoich urodzin: "))
mies=int(input("Podaj miesiąc swoich urodzin: "))
dzien=int(input("Podaj dzień swoich urodzin: "))
urodziny = datetime.datetime(rok,mies,dzien)

print("Urodziłeś się w:", urodziny.strftime("%A"))

print(wielkanoc())

input("\nAby zakończyć enter")
