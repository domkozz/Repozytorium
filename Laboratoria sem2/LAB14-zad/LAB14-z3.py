class Figura:
    def __init__(self, podstawa, bok, wysokosc, promien):
        self.podstawa = podstawa
        self.bok = bok
        self.wysokosc = wysokosc
        self.promien = promien

class Kwadrat(Figura):
    def __init__(self):
        super().__init__(int,0,0,0)
        self.podstawa = int(input("Podaj podstawe Kwadratu: "))
    def Pole(self):
        print("Pole kwadratu = ",self.podstawa**2)
    def Obw(self):
        print("Obwód kwadratu =",self.podstawa*4)

k = Kwadrat()
k.Pole()
k.Obw()

class Trojkat_Prostokatny(Figura):
    def __init__(self):
        super().__init__(int,0,int,0)
        self.podstawa = int(input("Podaj podstawe trójkąta: "))
        self.wysokosc = int(input("Podaj wysokość trójkąta:"))
    def Pole(self):
        print("Pole trójkąta = ",(self.podstawa*self.wysokosc)/2)
    def Obw(self):
        przekatna = int(input("Podaj przekątną: "))
        print("Obwód trójkąta =",self.podstawa+self.wysokosc+przekatna)

t = Trojkat_Prostokatny()
t.Pole()
t.Obw()

class Prostokat(Figura):
    def __init__(self):
        super().__init__(int,int,0,0)
        self.podstawa = int(input("Podaj podstawe prostokąta: "))
        self.bok = int(input("Podaj bok prostokąta:"))
    def Pole(self):
        print("Pole prostokąta = ",self.podstawa*self.bok)
    def Obw(self):
        print("Obwód prostokąta =",self.podstawa+self.bok)

p = Prostokat()
p.Pole()
p.Obw()

class Romb(Figura):
    def __init__(self):
        super().__init__(int,0,int,0)
        self.podstawa = int(input("Podaj podstawe Rombu: "))
        self.wysokosc = int(input("Podaj wysokość Rombu: "))
    def Pole(self):
        print("Pole Rombu = ",self.podstawa*self.wysokosc)
    def Obw(self):
        print("Obwód Rombu =",self.podstawa*4)

r = Romb()
r.Pole()
r.Obw()

class Kolo(Figura):
    def __init__(self):
        super().__init__(0,0,0,int)
        self.promien = int(input("Podaj promień koła: "))
    def Pole(self):
        print("Pole koła = ",(3.14)*(self.promien)**2)
    def Obw(self):
        print("Obwód koła =",self.promien*2*(3.14))

k = Kolo()
k.Pole()
k.Obw()