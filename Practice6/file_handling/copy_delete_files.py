# 1
f = open("Practice6/file_handling/myfile.txt", "x")
f.close()
with open("Practice6/file_handling/myfile.txt", "a") as f:
    f.write("This is a new file")

# 2
import shutil

shutil.copy("Practice6/file_handling/sample.txt", "Practice6/file_handling/myfile.txt")

# 3
with open("Practice6/file_handling/sample.txt", "r") as f:
    data = f.read()

with open("Practice6/file_handling/copy_sample.txt", "w") as f:
    f.write(data)

# 4
import os
os.remove("Practice6/file_handling/copy_sample.txt")

# 5
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")