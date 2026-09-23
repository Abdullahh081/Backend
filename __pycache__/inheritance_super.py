class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def describe(self):
        print(f"{self.name} is {self.age} years old.")


class Dog(Animal):              # Dog inherits from Animal
    def __init__(self, name, age, breed):
        super().__init__(name, age)   # calls Animal's __init__
        self.breed = breed            # Dog's own new attribute

    def bark(self):                   # Dog's own new method
        print(f"{self.name} says Woof!")


dog1 = Dog("Buddy", 3, "Labrador")

dog1.eat()        # Buddy is eating.       (inherited from Animal)
dog1.describe()   # Buddy is 3 years old.  (inherited from Animal)
dog1.bark()       # Buddy says Woof!       (defined in Dog)
print(dog1.breed) # Labrador