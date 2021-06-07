class samochod():
    def __init__(self,marka,model,przebieg,wartosc,kolor,rodzaj,):
        self.marka=marka
        self.model=model
        self.przebieg=przebieg
        self.wartosc=wartosc
        self.kolor=kolor
        self.rodzaj=rodzaj

    def jedzProsto(self):
        return ("Samochód o kolorze {} jedzie prosto z predkoscia ").format(self.kolor)
    def jedzLewo(self):
        return("Samochód marki {} jedzie w lewo").format(self.marka)
    def jedzPrawo(self):
        return ("Samochód marki {} o kolorze {} warty {} jedzie w prawo").format(self.marka,self.kolor,self.wartosc)
    def uruchomSilnik(self):
        return(("Samochód {} został uruchomiony")).format(self.marka)
    def wylaczSilnik(self):
        return (("Samochód {} został wyłączony")).format(self.marka)
samochod1 = samochod("BMW","X6","120,000km","200.000zł","Czarny","SUV")
samochod2 = samochod("Mercedes","C","20km","350.000zł","Czerwony","Coupe")
samochod3 = samochod("Alfa Romeo","Mito","20.000km","50.000zł","Czerwony","hatchback")
samochod4 = samochod("Audi","A7","20km","450.000zł","Srebrny","Coupe")
samochod5 = samochod("Porsche","911","5km","1.350.000zł","Czerwony","Coupe")
print(samochod1.jedzProsto())
print(samochod2.jedzLewo())
print((samochod3.jedzPrawo()))
print(samochod4.uruchomSilnik())
print(samochod5.wylaczSilnik())