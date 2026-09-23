class Dog:
    species = "Canine"   

    def __init__(self, name, age):
        self.name = name   
        self.age = age     

    def bark(self):        
        print(f"{self.name} says Woof!")

    def describe(self):    
        print(f"{self.name} is a {self.age}-year-old {self.species}")


dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

dog1.bark()       
dog2.describe()    