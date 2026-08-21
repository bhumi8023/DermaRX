class Animal:
    # colour = "White"  #like a static variable
    # breed = "husky"   #properties allowed to only class not to the object 
    # age= 3           #there is no constructor its called __init__ method
    # weight = 10

    # def __init__(self):   #it behaves as a constructor its not a constructor
    #         print("Hello,I am creating a object........")
    #         self.name="Sumit"
    #         self.age=20
    #         self.weight=50
    #         self.height=5.6
    #         self.breed="Owl"

    def __init__ (self, name, age, weight, height, breed):
           self.name = name
           self.age =  age
           self.weight = weight
           self.height = height
           self.breed = breed

    def __init__(self):
          self.name = ""
          self.age = ""
          self.id = ""

    def displaydata(self):
          print("My name is:",self.name)
          print("My age is:",self.age)
      
                
# print("Animal colour is:",Animal.colour) 
# print("Animal breed is:",Animal.breed) 

# a1 = Animal("Sumit",20,50,5,"Owl")
# print("Animal name is:",a1.name) 
# print("Animal age is:",a1.age) 
# print("Animal height is:",a1.height) 
# print("Animal weight is:",a1.weight) 
# print("Animal breed is:",a1.breed) 

# a2 = Animal("Atharva",21,50,5.3,"Chimpazee")
# print("Animal name is:",a2.name) 
# print("Animal age is:",a2.age) 
# print("Animal height is:",a2.height) 
# print("Animal weight is:",a2.weight) 
# print("Animal breed is:",a2.breed) 
a3 = Animal()
a3.name ="Bhoomika"
a3.age =20

a3.displaydata()
