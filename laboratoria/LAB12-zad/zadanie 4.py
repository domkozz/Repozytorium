def wysokosc(a):

    b=a/1000
    if a<5000:
        print(b,"km TO za nisko")
    else:
        print("Na tej wysokości jesteś bezpieczny")
    return(" ")

a=int(input("Podaj w metrach wysokość na jakiej lecimy: "))
print(wysokosc(a))