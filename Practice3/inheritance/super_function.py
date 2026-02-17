class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

class Parent():
    def __init__(self, name):
        self.name = name
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class Animal():
    def speak(self):
        print("Animal sound")

class Cat(Animal):
    def speak(self):
        super().speak()
        print("Meow")

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)