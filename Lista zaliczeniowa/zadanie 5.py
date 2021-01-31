def przelicznik(kwota,kurs):
    wynik=kwota*kurs
    return wynik
i=0
m=100000
x=0
z=0
print("Witaj w przeliczniku walut.")
if i<m:
    while x<m:
        decyzja = input("1 - przelicz walutę\n"
                        "2 - zakończ działanie programu\n"
                        "Wybierz 1 lub 2: ")

        if decyzja=="1":
            print("\nOto dostępne waluty, które możesz tu przeliczyć:\n"
                  "1.Baht tajski na Dolar Amerykański\n"
                  "2.Dolar Amerykański na Baht tajski\n"
                  "3.Bitcoin na Dolar Ameyrkański\n"
                  "4.Dolar Amerykański na Bitcoin\n"
                  "5.Ngultrum bhutański na Dolar Amerykański\n"
                  "6.Dolar Amerykański na Ngultrum bhutański\n"
                  "7.Ugija Mauretańska na Dolar Amerykański\n"
                  "8.Dolar Amerykański na Ugija mauretańska\n"
                  "9.Ethereum na Dolar Amerykański\n"
                  "10.Dolar Ameyrkański na Ethereum\n"
                  "11.Dram Armeński na Dolar Amerykański\n"
                  "12.Dolar Amerykański na Dram Armeński\n")
            while True:
                try:
                    wybor = int(input("Wybierz co chciałabyś przeliczyć: "))
                    break
                except ValueError:
                    print("Coś jest nie tak")
            if wybor in range(1,16):
                print("Przechodzimy do przeliczania!")
                i+=1
                if wybor == 1:
                    print("Wybrałeś opcję Baht na Dolar. W tej chwili 1 Baht tajski = 0.033 Dolara Amerykańskiego")
                    while True:
                        try:
                            kwota=float(input("Podaj ilość Bahtów: "))
                            kurs=0.33
                            print("W przeliczeniu na dolary to jest: ",przelicznik(kwota,kurs),"Dolarów Amerykańskich")
                            break
                        except ValueError:
                            print("To nie jest liczba")
                elif wybor == 2:
                    print("Wybrałeś opcję Dolar na Bath. W tej chwili 1 Dolar = 29.99 Bahtów")
                    while True:
                        try:
                            kwota = float(input("Podaj ilość Dolarów: "))
                            kurs = 29.99
                            print("W przeliczeniu na Bathy to jest: ", przelicznik(kwota, kurs), "Bahtów Tajskich")
                            break
                        except ValueError:
                            print("To nie jest liczba")

                elif wybor == 3:
                    print("Wybrałeś opcję Bitcoin na Dolar. W tej chwili 1 Bitcoin = 33 709.90 Dolarów Amerykanskich")
                    while True:
                        try:
                            kwota = float(input("Podaj ilość Bitcoinów: "))
                            kurs = 33709.90
                            print("W przeliczeniu na Dolary to jest: ", przelicznik(kwota, kurs),"Dolarów Amerykańskich")
                            break
                        except ValueError:
                            print("To nie jest liczba")

                elif wybor == 4:
                    print("Wybrałeś opcję Dolar na Bitcoin. W tej chwili 1 Dolar = 0.00002966 Bitcoina")
                    while True:
                        try:
                            kwota = float(input("Podaj ilość Dolarów: "))
                            kurs = 0.00002966
                            print("W przeliczeniu na Bitcoiny to jest: ", przelicznik(kwota, kurs),"Bitcoinów")
                            break
                        except ValueError:
                            print("To nie jest liczba")


                elif wybor == 5:
                    print("Wybrałeś opcję Ngultrum bhutański na Dolar. W tej chwili 1 Ngultrum bhutański = 0.014 Dolara Amerykańskiego")
                    while True:
                        try:
                            kwota = float(input("Podaj ilość Ngultrumów bhutańskich: "))
                            kurs = 0.14
                            print("W przeliczeniu na Dolary to jest: ", przelicznik(kwota, kurs),"Dolarów Amerykańskich")
                            break
                        except ValueError:
                            print("To nie jest liczba")

                elif wybor == 6:
                    print("Wybrałeś opcję Dolar na Ngultrum bhutański. W tej chwili 1 Dolar = 72.81 Ngultrumów bhutańskich")
                    while True:
                       try:
                            kwota = float(input("Podaj ilość Dolarów: "))
                            kurs = 72.81
                            print("W przeliczeniu na Ngultrumy to jest: ", przelicznik(kwota, kurs),"Ngultrumów bhutańskich")
                            break
                       except ValueError:
                           print("To nie jest liczba")

                elif wybor == 7:
                    print("Wybrałeś opcję Ugija mauretańska na Dolar. W tej chwili 1 Ugija = 0.02776235 Dolara Amerykańskiego")
                    while True:
                        try:
                            kwota = float(input("Podaj ilość Ugiji: "))
                            kurs = 0.02776235
                            print("W przeliczeniu na Dolary to jest: ", przelicznik(kwota, kurs),"Dolarów Amerykańskich")
                            break
                        except ValueError:
                            print("To nie jest liczba")

                elif wybor == 8:
                    print("Wybrałeś opcję Dolar na Ugija Mauretańska. W tej chwili 1 Dolar = 36.02 Ugiji Mauretańskich")
                    while True:
                        try:
                            kwota = float(input("Podaj ilość Dolarów: "))
                            kurs = 36.02
                            print("W przeliczeniu na ugije to jest: ", przelicznik(kwota, kurs),"Ugiji Mauretańskich")
                            break
                        except ValueError:
                            print("To nie jest liczba")

                elif wybor == 9:
                    print("Wybrałeś opcję Ethereum na Dolar. W tej chwili 1 Ethereum = 1 382.69 Dolarów Amerykańskich")
                    while True:
                        try:
                            kwota = float(input("Podaj ilość Ethereum: "))
                            kurs = 1382.69
                            print("W przeliczeniu na Dolary to jest: ", przelicznik(kwota, kurs),"Dolarów Amerykańskich")
                            break
                        except ValueError:
                            print("To nie jest liczba")

                elif wybor == 10:
                    print("Wybrałeś opcję Dolar na Ethereum. W tej chwili 1 Dolar = 0.00072323 Ethereum")
                    while True:
                        try:
                            kwota = float(input("Podaj ilość Dolarów: "))
                            kurs = 0.00072323
                            print("W przeliczeniu na Ethereum to jest: ", przelicznik(kwota, kurs),"Ethereum")
                            break
                        except ValueError:
                            print("To nie jest liczba")

                elif wybor == 11:
                    print("Wybrałeś opcję Dram Armeński na Dolar. W tej chwili 1 Dram = 0.0019 Dolara")
                    while True:
                        try:
                            kwota = float(input("Podaj ilość Dramów: "))
                            kurs = 0.0019
                            print("W przeliczeniu na Dolary to jest: ", przelicznik(kwota, kurs),"Dolarów Amerykańskich")
                            break
                        except ValueError:
                            print("To nie jest liczba")

                elif wybor == 12:
                    print("Wybrałeś opcję Dolar na Dram Armeński. W tej chwili 1 Dolar = 518.36 Dramów Armeńskich")
                    while True:
                        try:
                            kwota = float(input("Podaj ilość Dolarów: "))
                            kurs = 518.36
                            print("W przeliczeniu na Dramy to jest: ", przelicznik(kwota, kurs),"Dramów Armeńskich")
                            break
                        except ValueError:
                            print("To nie jest liczba")
                elif wybor > 12:
                    print("Wybrana opcja nie istnieje")
            else:
                print("Jeszcze raz.")
        elif decyzja=="2":
            x+=m
        elif decyzja!="1" or decyzja!="2":
            print("Coś poszło nie tak. Wybierz ponownie.")