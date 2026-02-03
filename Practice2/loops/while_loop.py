i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

i = 5
word = "Hello"
while i < 5:
    print(word)
    i -= 1

i = 0
word = "Hello, world!"
while i < 13:
    print(word[i], end = "-")
    i += 1

num = 13
while num % 2 != 0:
    print(f"{num} is not even yet")
    num -= 1
print(f"{num} is already even")