def cel_far(temperatura):
    far=temperatura*9/5+32
    if far<=32:
        print("Woda zamarza.Temperatura w stopniach Fahrenheita wynosi: ",far,"F")
    elif far>32 and far<212:
        print("Temperatura w stopniach Fahrenheita wynosi: ", far, "°F")
    elif far>=212:
        print("Woda wrze.Temperatura w stopniach Fahrenheita wynosi: ", far, "°F")
    return(" ")

def far_kel(temperatura):
    kel = ((temperatura - 32)/1.8000) + 273.15
    print("Temperatura w stopniach Kelwina Wynosi: ",kel,"K")
    return(" ")

def kel_far(temperatura):
    far = ((temperatura - 273.15)*1.8000) + 32
    print("Temperatura w stopniach Fahrenheita wynosi: ", far,"°F")
    return(" ")

def cel_deli(temperatura):
    deli = (100 - temperatura) * (3/2)
    print("Temperatura w stopniach Delisle’a wynosi: ", deli, "°D")

def deli_cel(temperatura):
    cel = 100 - temperatura  *(2/3)
    print("Temperatura w stopniach Celsjusza wynosi: ", cel, "°C")
    return (" ")

def cel_kel(temperatura):
    kel = temperatura + 273.15
    print("Temperatura w stopniach Kelwina wynosi: ", kel, "K")
    return (" ")

def kel_cel(temperatura):
    cel = temperatura - 273.15
    print("Temperatura w stopniach Celsjusza wynosi: ", cel,"°C")
    return (" ")



i=0
while i<1:
    print("\nPrzelicznik skal temperatur.Wybierz z jakiej skali chcesz przeliczyć: "
          "\n1. Z Celsjusza na Fahrenheita"
          "\n2. Z Fahrenheita na Kelwina"
          "\n3. Z Kelwina na Fahrenheita"
          "\n4. Z Celsjusza na Delisle’a"
          "\n5. Z Delisle’a na Celsjusza"
          "\n6. Z Celsjusza na Kelwina"
          "\n7. Z Kelwina na Celsjusza"
          "\nLUB"
          "\n8. Zakończ działanie programu")
    wybor=input("\nWybierz co chcesz zrobić: ")
    if wybor=="1":
        while True:
            try:
                temperatura=float(input("Podaj Temperaturę w stopniach Celsjusza: "))
                print(cel_far(temperatura))
                break
            except ValueError:
                print("Coś jest nie tak.")
        input("\nNaciśnij enter,aby wrócić do Menu")
    elif wybor=="2":
        while True:
            try:
                temperatura = float(input("Podaj Temperaturę w stopniach Fahrenheita: "))
                print(far_kel(temperatura))
                break
            except ValueError:
                print("Coś jest nie tak.")
        input("\nNaciśnij enter,aby wrócić do Menu")
    elif wybor=="3":
        while True:
            try:
                temperatura = float(input("Podaj Temperaturę w stopniach Kelwina: "))
                print(kel_far(temperatura))
                break
            except ValueError:
                print("Coś jest nie tak.")
        input("\nNaciśnij enter,aby wrócić do Menu")
    elif wybor=="4":
        while True:
            try:
                temperatura = float(input("Podaj Temperaturę w stopniach Celsjusza: "))
                print(cel_deli(temperatura))
                break
            except ValueError:
                print("Coś jest nie tak.")
        input("\nNaciśnij enter,aby wrócić do Menu")
    elif wybor=="5":
        while True:
            try:
                temperatura = float(input("Podaj Temperaturę w stopniach Delisle'a: "))
                print(deli_cel(temperatura))
                break
            except ValueError:
                print("Coś jest nie tak.")
        input("\nNaciśnij enter,aby wrócić do Menu")
    elif wybor=="6":
        while True:
            try:
                temperatura = float(input("Podaj Temperaturę w stopniach Celsjusza: "))
                print(cel_kel(temperatura))
                break
            except ValueError:
                print("Coś jest nie tak.")
        input("\nNaciśnij enter,aby wrócić do Menu")
    elif wybor=="7":
        while True:
            try:
                temperatura = float(input("Podaj Temperaturę w stopniach kelwina: "))
                print(kel_cel(temperatura))
                break
            except ValueError:
                print("Coś jest nie tak.")
        input("\nNaciśnij enter,aby wrócić do Menu")
    elif wybor=="8":
        i+=1
    else:
        print("Coś poszło nie tak.")
