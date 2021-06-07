class ksiazka():
    def __init__(self,tytul,autor,iloscStron,rokProdukcji,opisFabuly):
        self.tytul = tytul
        self.autor = autor
        self.iloscStron = iloscStron
        self.rokProdukcji = rokProdukcji
        self.opisFabuly = opisFabuly

    def opis(self):
        print("Książka:",self.tytul,"\nOpis fabuły:",self.opisFabuly)

    def rokWydania(self):
        print("\nRok wydania",self.tytul,": ",self.rokProdukcji)
    def otworzKsiazke(self,strona):
        print("Otworz ksiazke",self.tytul,"na stronie:",strona)
    def ocenKsiazke(self):
        x = int(input("Oceń książkę w skali 0/10: "))
        if x<4:
            print("Książka musi być słaba")
        elif x>=4 and x<=6:
            print("Książka jest nienajgorsza, ale nie porywa")
        else:
            print("Książka musi być mega dobra")
ksiazki = list()

ksiazka1 = ksiazka("Hobbit", "J.R.R. Tolkien", "500", "1937","Hobbit Bilbo Baggins wyrusza w niebezpieczną podroż by wraz z czarodziejem Gandalfem i trzynastoma krasnoludami pokonać smoka Smauga.")

ksiazka2 = ksiazka("Harry Potter", "J.K. Rowling", "400", "1997","Cykl przedstawia świat magii,"
" czyli społeczność czarodziejów, istniejącą równolegle do świata niemagicznego, tak zwanego mugolskiego.")

ksiazka3 = ksiazka("Mały książę", "Antoine de Saint-Exupéry", "250", "1943","Mały Książę jest książką opowiadającą o dorastaniu do wiernej miłości,"
" do prawdziwej przyjaźni i odpowiedzialności za drugiego człowieka. Stawia pytania o hierarchię wartości czy sens więzi między ludźmi.")

ksiazka4 = ksiazka("W pustyni i w puszczy", "Henryk Sienkiewicz", "310", "1911","Główny wątek utworu dotyczy porwania dwojga dzieci przez zwolenników Mahdiego."
" Po uwolnieniu się z rąk porywaczy, dzieci przemierzają Afrykę w poszukiwaniu pomocy, doświadczając wielu ekscytujących przygód.")

ksiazki.append((ksiazka1))
ksiazki.append((ksiazka2))
ksiazki.append((ksiazka3))
ksiazki.append((ksiazka4))

ksiazka1.opis()
ksiazka2.rokWydania()
ksiazka3.otworzKsiazke(150)
ksiazka4.ocenKsiazke()











# ksiazki=list()
# ksiazka1=ksiazka("Hobbit","J.R.R. Tolkien","500","1937")
# ksiazka2=ksiazka("Harry Potter","J.K. Rowling","400","1997")
# ksiazka3=ksiazka("Mały książę","Antoine de Saint-Exupéry","250","1943")
# ksiazka4=ksiazka("W pustyni i w puszczy","Henryk Sienkiewicz","310","1911")
# ksiazki.append((ksiazka1))
# ksiazki.append((ksiazka2))
# ksiazki.append((ksiazka3))
# ksiazki.append((ksiazka4))

