# 1
with open("Practice6/file_handling/sample.txt", "a") as f:
    f.write("\n")


# 2
with open("Practice6/file_handling/sample.txt", "w") as f:
    f.write("Write new text, but delete previous one")

# 3
with open("Practice6/file_handling/sample.txt", "r") as f:
    data = f.read()

data = data.replace(" ", "/")

with open("Practice6/file_handling/sample.txt", "w") as f:
    f.write(data)

# 4
with open("Practice6/file_handling/sample.txt", "a") as f:
    f.write("/New txt")

# 5
with open("Practice6/file_handling/sample.txt", "r") as f:
    data = f.read()

data = data.upper()

with open("Practice6/file_handling/sample.txt", "w") as f:
    f.write(data)