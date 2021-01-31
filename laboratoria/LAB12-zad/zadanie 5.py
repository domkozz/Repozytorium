def bmi(masa,wzrost):
    bmi=masa/wzrost**2
    print(bmi)
    if bmi<18.5:
        print("Masz niedowagę")
    elif bmi>=18.5 and bmi<24.99:
        print(("Waga prawidłowa"))
    elif bmi>=25:
        print("Masz nadwage")
    return (" ")

masa=float(input("Podaj swoja mase w kg: "))
wzrost=float(input("Podaj swoj wzrost w metrach(np. 1.87): "))
print(bmi(masa,wzrost))