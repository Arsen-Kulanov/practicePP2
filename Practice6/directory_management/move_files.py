# 1
import shutil

shutil.move("sample.txt", "Practice6/file.txt")

# 2
from pathlib import Path

source = Path("source")
destination = Path("txt_files")

destination.mkdir(exist_ok=True)

for file in source.glob("*.txt"):
    shutil.move(str(file), destination / file.name)

# 3
source = Path("downloads")

for file in source.iterdir():
    if file.is_file():
        ext = file.suffix[1:]
        
        folder = source / ext
        folder.mkdir(exist_ok=True)
        
        shutil.move(file, folder / file.name)

# 4
source = Path("data")
destination = Path("big_files")

destination.mkdir(exist_ok=True)

for file in source.iterdir():
    if file.is_file() and file.stat().st_size > 1024 * 1024:
        shutil.move(file, destination / file.name)

# 5
from pathlib import Path
import shutil

file = Path("example.txt")
destination = Path("archive/example.txt")

if file.exists():
    destination.parent.mkdir(exist_ok=True)
    shutil.move(file, destination)
    print("File moved!")
else:
    print("File not found")