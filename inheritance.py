class Animal:

    def __init__(self,species):
        self.species = species
        print("Here in animal class")
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def __init__(self, species,name,colour,age,breed):
        super().__init__(species)  #super is used to know anthing from parent class
        print("Here in Dog class")
        self.name = name
        self.colour = colour
        self.age = age
        self.breed = breed

    def sound(self):
        print("Bhau bhau")


d1 = Dog("Dog","Oreo","Black",2,"Husky")
#1.__init__("Dog","Oreo","Black",2,"Husky")
d1.sound()
 


     