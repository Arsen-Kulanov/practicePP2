i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

while True:
    x = int(input("Enter a number: (0 - exit)"))
    if x == 0:
        break
    print(x * 2)

i = 10
while i > 0:
    if i == 3:
        break
    print(i)
    i -= 1

text = ""
while True:
    text = input("Enter a word: ")
    if text == "stop":
        break
    print(text)

i = 0
while i < 100:
    if i == 20:
        break
    print(i)
    i += 4