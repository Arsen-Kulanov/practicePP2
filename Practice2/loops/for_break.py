fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

for x in fruits:
    if x == "banana":
        break
    print(x)

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

for char in "hello world":
    if char == " ":
        break
    print(char)

nums = [1, 3, 5, 7, 9, 11]
for n in nums:
    if n == 7:
        break
    print(n)

for i in range(100):
    if i > 10:
        break
    print(i)