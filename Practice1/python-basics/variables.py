x = 5
y = "John"
print(x)
print(y)

x = 4      
x = "Sally" 
print(x)

x = str(3)    
y = int(3)    
z = float(3)

x = 5
y = "John"
print(type(x))
print(type(y))

# Variable Names

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Each word, except the first, starts with a capital letter: Camel Case
myVariableName = "John"
# Each word starts with a capital letter: Pascal Case
MyVariableName = "John"
# Each word is separated by an underscore character: Snake Case
my_variable_name = "John"

# Assign Multiple Values

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)
# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

# Global Variables

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
# Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

