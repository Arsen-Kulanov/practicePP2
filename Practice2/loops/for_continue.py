fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

for i in range(10):
    if i == 5:
        continue
    print(i)

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

for char in "python":
    if char == "o":
        continue
    print(char, end = "")

print("")
nums = [2, 4, 6, 7, 8]
for n in nums:
    if n % 2 == 0:
        continue
    print(n)

for i in range(10):
    if i < 3:
        continue
    print(i)