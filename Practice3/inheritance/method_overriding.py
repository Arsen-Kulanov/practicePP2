class Animal():
    def speak(self):
        print("Animal sound")
class Dog(Animal):
    def speak(self):
        print("Woof")

class Shape():
    def area(self):
        return 0
class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5
    
class Person():
    def info(self):
        print("Person")
class Student(Person):
    def info(self):
        print("Student")

class BankAccount():
    def withdraw(self, amount):
        print("Withdrawing", amount)
class SafeAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 1000:
            print("Limit exceeded")
        else:
            print("Withdrawing", amount)

class Bird():
    def fly(self):
        print("Flying")
class Penguin(Bird):
    def fly(self):
        print("Cannot fly")