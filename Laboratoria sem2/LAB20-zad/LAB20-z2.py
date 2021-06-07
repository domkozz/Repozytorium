waga = int(input("Podaj wagę: "))
wzrost = int(input("Podaj wzrost: "))
wiek = int(input("Podaj wiek: "))
plec = str(input("Podaj płeć (Mężczyzna/Kobieta): "))

assert plec == "Mężczyzna" or plec =="Kobieta", "Wybierz poprawnie płeć"

if plec =="M":
    bmr = round(66 + (13.7 * waga) + (5 * wzrost) - (6.76 * wiek))
else:
    bmr = round(655 + (9.6 * waga) + (1.8 * wzrost) - (4.7 * wiek))

print("Wynik BMR to: ", bmr)