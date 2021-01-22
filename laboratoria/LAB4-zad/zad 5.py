while True:

    x = float(input("Podaj liczbę: "))

    if x == 0:

        break

    else:

        liczby.append(x)

        print(liczby)

        i = 0

        suma = 0.0

        dlug = float(len(liczby))

        while i < dlug-1:

            suma = suma + liczby[i]

            i+=1

        print(suma/dlug)
