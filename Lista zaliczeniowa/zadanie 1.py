def skladki_spoleczne(kwota):
    emerytalna = kwota * 0.0976
    rentowa = kwota * 0.015
    chorobowa = kwota * 0.0245
    skladka1 = emerytalna + rentowa + chorobowa
    print("\nWyliczenie składek społecznych:")
    print("Składka emerytalna(9,76%) wynosi:", emerytalna, "zł")
    print("Składka rentowa(1,5%) wynosi:", rentowa, "zł")
    print("Składka chorobowa(2,45%) wynosi:", chorobowa, "zł\n\nSuma składek społecznych to: ",skladka1, "zł\n")
    return (" ")

def skladki_zdrowotne(kwota):
    emerytalna = kwota * 0.0976
    rentowa = kwota * 0.015
    chorobowa = kwota * 0.0245
    skladka1 = emerytalna + rentowa + chorobowa
    kwota2 = kwota - skladka1
    zdrowotna = kwota2 * 0.09
    zdrowotna2 = kwota2 * 0.0775
    print("Wyliczenie składek zdrowotnej:\n"
          "Składka zdrowotna(9% całościowa): ", zdrowotna, "zł\n"
          "Składka zdrowotna(7,5% podlegająca odliczeniu): ",
          zdrowotna2, "zł")
    return (" ")

def podatek_dochodowy(kwota):
    emerytalna = kwota * 0.0976
    rentowa = kwota * 0.015
    chorobowa = kwota * 0.0245
    skladka1 = emerytalna + rentowa + chorobowa
    kwota2 = kwota - skladka1  # kwota po odliczeniu składki społecznej
    zdrowotna = kwota2 * 0.09  # składka zdrowotna w całości
    zdrowotna2 = kwota2 * 0.0775  # składka zdrowotna podlegająca odliczeniu
    kp = 250  # koszty uzyskania przychodów
    kwota3 = kwota2 - kp  # podstawa opodatkowania
    k = kwota3 * 0.17  # podatek należny
    k2 = k - 43.76  # podatek należny pomniejszony o kwotę wolną od podatku
    z = k2 - zdrowotna2  # zaliczka na podatek dochodowy
    x = 169
    print("\nWyliczenie podatku dochodowego:\n"
          "Jest on uzależniony od składki zdrowotnej która w tym przypadku wynosi:"
          "Podatek należny: ", k, "zł\n"
          "Podatek należny pomniejszony o kwotę wolną od podatku: ",k2, "zł")
    print("Zaliczka na podatek dochodowy wynosi:",z, "czyli w zaokrągleniu:",x, "zł",
          "\nobliczenie podatku dochodowego jest zależne od składki zdrowotnej wynoszącej w tym wypadku: ",zdrowotna,"zł")
    return (" ")

def netto(kwota):
      emerytalna = kwota * 0.0976
      rentowa = kwota * 0.015
      chorobowa = kwota * 0.0245
      skladka1 = emerytalna + rentowa + chorobowa
      kwota2 = kwota - skladka1  # kwota po odliczeniu składki społecznej
      zdrowotna = kwota2 * 0.09  # składka zdrowotna w całości
      zdrowotna2 = kwota2 * 0.0775  # składka zdrowotna podlegająca odliczeniu
      kp = 250  # koszty uzyskania przychodów
      kwota3 = kwota2 - kp  # podstawa opodatkowania
      k = kwota3 * 0.17  # podatek należny
      k2 = k - 43.76  # podatek należny pomniejszony o kwotę wolną od podatku
      z = k2 - zdrowotna2  # zaliczka na podatek dochodowy
      x = 169
      netto = kwota2 - x - zdrowotna
      print(skladki_spoleczne(kwota), skladki_zdrowotne(kwota), podatek_dochodowy(kwota))
      print("\nPrzechodzimy do końcowego ustalenia wynagrodzenia netto.\n"
      "które wynosi po wszystkich wyliczeniach: ",netto,"zł.\n"
      "Kwota netto to: brutto-składka społeczna-składka zdrowotna(9%)-podatek dochodowy.")
      return (" ")

print("Witam Cię w kalkulatrze wynagrodzenia twojego wynagrodzenia netto.\n"
      "Program zakłada zatrudnienie poprzez umowę o pracę.")
while True:
    try:
        wybor = int(input("Co chciałabyś obliczyć/zrobić?\n"
                    "1.Składki społeczne\n"
                    "2.Składki zdrowotne\n"
                    "3.Podatek dochodowy\n"
                    "4.Wynagrodzenie netto ze wszystkimi wyliczeniami\n"
                    "\n\nWybierz aktywność: "))
        break
    except ValueError:
        print("Coś poszło nie tak.")
kasa = int(input("Podaj twoje wynagrodzenie brutto: "))
if wybor==1:
      print(skladki_spoleczne(kasa))
elif wybor==2:
      print(skladki_zdrowotne(kasa))
elif wybor==3:
      print(podatek_dochodowy(kasa))
elif wybor==4:
      print(netto(kasa))
input("\nAby zakończyć naciśnij enter")
