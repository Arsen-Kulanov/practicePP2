i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

i = 0
while i <= 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print("i : ", i)

i = 1
while i <= 5:
    if i == 2:
        i += 1
        continue
    print(i)
    i += 1

i = 0
while i < 8:
    i += 1
    if i > 5:
        continue
    print(i)