# 1
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
for i in y:
    print(i)

# 2
x = (1, 2, 3)
y = (4, 5, 6)
z = zip(x, y)
for i in z:
    print(i)

# 3
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")
c = (1, 2, 3)

x = zip(a, b, c)
for i in x:
    print(i)

# 4
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

for name, score in zip(names, scores):
    print(name, score)

# 5
fruits = ["apple", "banana", "orange"]

for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)