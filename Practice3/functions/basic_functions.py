def my_function():
    print("Hello from a function")
my_function()

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

def var_type(a):
    print("Variable type is", type(a))
var_type(5)

def loop():
    for i in range(5):
        print(i)
loop()

# function placeholder without any code
def func():
    pass