class Dog:
    def __init__(self, name, age):
        # These are instance attributes
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")


# Creating instances
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.name)   
print(dog2.name)  

dog1.bark()         
dog2.bark()         