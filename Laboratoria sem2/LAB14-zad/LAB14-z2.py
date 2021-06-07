class Animal:
    def __init__(self,name,specie_type,move):
        self.name = name
        self.specie_type=specie_type
        self.move = move
    def printname(self):
        print ("Nazwa :",self.name)
    def printspecie(self):
        print ("Rasa to:",self.specie_type)
    def moving(self):
        print(self.name+" "+self.move)

class Dog(Animal):
    pass

dog1 = Dog("Pies","husky","biegnie")
dog1.printname()
dog1.printspecie()


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self,"Kot","MaineCoon","biegnie")
cat1=Cat()
cat1.printname()
cat1.printspecie()

class Fish(Animal):
    pass
fish=Fish("Ryba","Golden","pływa")
fish.moving()

class Bird(Animal):
    pass
bird=Bird("Ptak","Eagle","Lata")
bird.moving()