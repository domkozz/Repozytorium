print("Liczenie średniej arytmetycznej floatów i intów nieujemnych")
n=int(input("podaj ilość liczb: "))
suma=0
i=0
inty=0
il_int=0
floaty=0
il_float=0
while i!=n:
    a=float(input("podaj liczbe: "))
    if a.is_integer():
        inty+=a
        il_int+=1
        i+=1
    else:
        floaty+=a
        il_float+=1
        i+=1
    if a<0:
        print("musi być nieujemna")
        i-=1
        continue
    suma=inty+floaty
print("ilość intów i floatów to odpowiednio",il_int,"i",il_float,"a suma arytmetyczna podanych liczb to",suma/n)
input("\nAby zakończyć naciśnij enter")
