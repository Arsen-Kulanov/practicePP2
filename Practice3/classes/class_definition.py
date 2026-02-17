# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

class MyClass():
    x = 5 
p1 = MyClass()
print(p1.x)

del p1

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Tobias", 25)
print(p1.age)

p1.age = 26
print(p1.age)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Linus", 30)

del p1.age

print(p1.name) # This works
# print(p1.age) # This would cause an error