while True:
    a = int(input("Podaj liczbe: "))
    b = int(input("Podaj liczbe: "))
    c = int(input("Podaj liczbe: "))
    d = int(input("Podaj liczbe: "))
    if a  == 0:
        print("liczba a to 0")
        break
    else:
        if b == 0:
            print("liczba b to 0")
            break
        else:
            if c == 0:
                print("liczba c to 0")
                break
            else:
                if d == 0:
                    print("liczba d to 0")
                    break
                else:
                     print(a+b+c+d/4)
