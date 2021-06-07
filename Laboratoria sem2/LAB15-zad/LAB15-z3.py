class Obywatel:
    def __init__(self,imie="",nazwisko="",ulica="",nr_domu="",kod_pocztowy="",miejscowosc=""):
        self.imie = imie
        self.nazwisko = nazwisko
        self.ulica = ulica
        self.nr_domu = nr_domu
        self.kod_pocztowy = kod_pocztowy
        self.miejscowosc = miejscowosc

    def set_dane(self):
        self.imie = input("Podaj imie: ")
        self.nazwisko = input("Podaj Nazwisko: ")
        self.miejscowosc = input("Podaj Miejscowość: ")
        self.ulica = input("Podaj Ulice: ")
        self.nr_domu = input("Podaj numer domu: ")
        self.kod_pocztowy = input("Podaj kod pocztowy: ")

    def get_wizytowka(self):
        print("Tak prezentuje się twoja wizytówka:\n")
        print("--------------------------")
        print(self.imie+" "+self.nazwisko)
        print("ul."+self.ulica,"/ nr.domu",self.nr_domu)
        print(self.kod_pocztowy,self.miejscowosc)
        print("--------------------------")




typek = Obywatel()
typek.set_dane()
typek.get_wizytowka()
