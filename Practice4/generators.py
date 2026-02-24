# 1
def generator(n):
    for i in range(n+1):
        yield i**2

for num in generator(5):
    print(num)

# 2
def even(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input())
print(*generator(n), sep = ", ")

# 3
def div(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for num in div(n):
    print(num)

# 4
def squares(a, b):
    for i in range(a, b+1):
        yield i**2

a = int(input())
b = int(input())
for num in squares(a, b):
    print(num)

# 5
def generator(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
for num in generator(n):
    print(num)