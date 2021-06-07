try:
    dd=int(input("Podaj pierwsze 2 cyfry kodu pocztowego: "))
    if dd in range(0,100) or dd==00:
        ddd=int(input("Podaj 3 kolejne cyfry kodu pocztowego:  "))
        if ddd in range(0,1000) or ddd==000:
            kod_pocztowy= dd+ddd
            z = str(dd)+"-"+str(ddd)
        if kod_pocztowy <=540 and kod_pocztowy>=0:
            print("Kod pocztowy:",z," poprawny")
    else:
        print("Nie ma takiego kodu")

except ValueError:
    print("Przepraszam, ale coś jest nie tak\n"
          "możliwy niepoprawny kod pocztowy")

