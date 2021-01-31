def pojemnosc(gb):
    dziesiatkowy=gb*1000**3
    dwojkowy=dziesiatkowy/1024/1024/1024
    print("Realna pojemność tego dysku wynosi: ",dwojkowy,"GB")
    return(" ")

i=0

print("Hej, chcesz sprawdzić realną pojemność swojego dysku?\n"
      "Jeśli tak to dobrze trafiłeś. Poniżej zostanie wytłumaczone, gdzie znikają twoje GB ;)\n\n")
print("W systemie dziesiątkowym, 1KB = 1000 bajtów,"
      "czyli dysk twardy o nominalnej pojemności 500GB będzie się składać z:\n"
      "500 bajtów x 1000 kilobajtów x 1000 megabajtów x 1000 gigabajtów = 500 000 000 000 bajtów.\n"
      "skoro rozłożyliśmy dysk na bajty,\n"
      "czas przełożyć nasz wynik na system dwójkowy, w którym to 1KB = 1024 bajty.\n"
      "Proces przebiega odwrotnie do powyższego przykładu, deklarowane 500GB, czyli 500 000 000 000 \n"
      "bajtów dzielimy trzykrotnie przez 1024, więc 500 000 000 000 / 1024 / 1024 / 1024 = 465,66GB\n"
      "Tym prostym sposobem doszliśmy do tego, jak i dlaczego z nominalnych 500GB mamy do użytku tylko 465GB.")
print("\n\nTeraz jeśli chcesz możesz sprawdzić jaką realną pojemność ma twój dysk lub zakończyć działanie programu.\n")
while i<1:
    print('1.Sprawdź pojemność\n'
           'Lub\n'
           '2.Zakończ działanie\n')
    wybor=input("Wybierz co chcesz zrobić: ")
    if wybor=="1":
        while True:
            try:
                gb = float(input("Podaj pojemność dysku w GB: "))
                break
            except ValueError:
                print("Coś poszło nie tak. :/")
        print(pojemnosc(gb))
    elif wybor=="2":
        i+=1
    else:
        print("\nNie ma takiej opcji.\n")
