import math

# 1
degree = int(input("Input degree: "))
print("Output radian:", math.radians(degree))

# 2
height = int(input("Height: "))
base1 = int(input("Base, first value: "))
base2 = int(input("Base, second value: "))
print("Expected Output:", (base1+base2)/2 * height)

# 3
sides = int(input("Enter a number of sides: "))
length = int(input("Enter a length of a side: "))
print("The area of the polygon is:", round((sides * length ** 2) / (4 * math.tan(math.pi / sides))))

# 4
base = int(input("Length of base: "))
height = int(input("Height of parallelogram: "))
print("Expected Output:", base*height)