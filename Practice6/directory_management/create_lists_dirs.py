# 1
import os

os.makedirs("project/data/raw", exist_ok=True)
os.makedirs("project/data/processed", exist_ok=True)
os.makedirs("project/logs", exist_ok=True)

# 2 
path = "project"
for item in os.listdir(path):
    print(item)

# 3
for root, dirs, files in os.walk("project"):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root, file))

# 4
from pathlib import Path

p = Path("project/data/file.txt")
print(p)
print(f"Created {p.stem} with extension {p.suffix} in {p.parent}")

# 5
p = Path("project/data/file.txt")
if p.exists():
    if p.is_file():
        print("file!")
    elif p.is_dir():
        print("dir!")
    else:
        print("undefined")
else:
    print("Doesnt exist")