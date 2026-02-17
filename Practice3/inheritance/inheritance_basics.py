class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

class Animal():
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()

class Vehicle():
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

c = Car()
c.start()
c.drive()

class Person():
    def __init__(self, name):
        self.name = name

class Student(Person):
    def study(self):
        print(self.name, "is studying")

s = Student("Arsen")
s.study()

class Employee():
    def __init__(self, salary):
        self.salary = salary

class Manager(Employee):
    def __init__(self, salary, bonus):
        self.bonus = bonus
        super().__init__(salary)

m = Manager(5000, 1000)
print(m.salary, m.bonus)