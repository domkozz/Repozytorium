def koszty_pracodawcy(kwota):
    emerytalna = kwota * 0.0976
    rentowa = kwota * 0.065
    chorobowa = kwota * 0.0245
    wypadkowa = kwota * 0.0167
    fgsp = kwota * 0.001
    skladka1 = emerytalna + rentowa + chorobowa + wypadkowa + fgsp
    print("Koszty osobno:\nSkładka emerytalna(9.76%) wynosi: ",emerytalna,"zł\nSkładka rentowa(6.5%) wynosi: ",rentowa,
          "zł\nSkładka chorobowa(2.45%) wynosi: ",chorobowa,"zł\nSkładka wypadkowa(1.67%) wynosi: ",
          wypadkowa,"zł\nSkładka FGŚP(0.1%) wynosi: ",fgsp,"zł")
    print("\nKoszty związane z zatrudnieniem pracownika przy tej stawce brutto razem wynoszą: ",skladka1,"zł")
    return(" ")

print("Witam Cię w kalkulatrze kosztów zatrudnienia pracownika.\n"
      "Kalkulator bierze pod uwagę tylko umowę o pracę\n")

while True:
    try:
        kwota = float(input("Podaj wynagrodzenie brutto pracownika: "))
        break
    except ValueError:
        print("Coś poszło nie tak")
print(koszty_pracodawcy(kwota))
input("\nAby zakończyć wciśnij enter")