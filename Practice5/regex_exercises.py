import re

with open("Practice5/sample.txt", "r", encoding="utf-8") as f:
    exmp = f.read()

# 1
pattern = r"\bab*\b"
print(bool(re.search(pattern, exmp)))

# 2
pattern = r"\bab{2,3}\b"
print(bool(re.search(pattern, exmp)))

# 3
pattern = r"\b[a-zа-я]+(?:_[a-zа-я]+)+\b"
print(*re.findall(pattern, exmp), sep="\n")

# 4
pattern = r"\b[A-ZА-Я][a-zа-я]+\b"
print(*re.findall(pattern, exmp), sep="\n")

# 5
pattern = r"^a.*b$"
print(*re.findall(pattern, exmp, re.MULTILINE), sep="\n")

# 6
result = re.sub(r"[ ,\.]", ":", exmp)
print(result)

# 7
def to_camel(s):
    return re.sub(r"_([a-z])", lambda m: m.group(1).upper(), s)

print(to_camel(exmp))

# 8
pattern = r"(?=[A-ZА-Я])"
result = re.split(pattern, exmp)
print(*result, sep="\n")

# 9
result = re.sub(r"(?<!^)([A-ZА-Я])", r" \1", exmp)
print(result)

# 10
result = re.sub(r"(?<!^)([A-ZА-Я])", r"_\1", exmp).lower()
print(result)