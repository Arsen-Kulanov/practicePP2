# 1
f = open("Practice6/file_handling/sample.txt", "r")
print(f.read())

# 2
print(f.readline())
f.close()

# 3
with open("Practice6/file_handling/sample.txt") as f:
    print(f.read(5))

# 4
with open("Practice6/file_handling/sample.txt") as f:
    for x in f:
        print(x)

# 5
with open("Practice6/file_handling/sample.txt") as f:
    for i in range(10):
        print(f.readline(i))