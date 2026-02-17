students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

words = ["apple", "kiwi", "banana"]
result = sorted(words, key=lambda w: len(w))
print(result)

people = [
    {"name": "Arsen", "age": 20},
    {"name": "Anna", "age": 18},
    {"name": "Mike", "age": 25}
]

result = sorted(people, key=lambda x: x["age"])
print(result)

nums = [5, 1, 9, 3]
result = sorted(nums, key=lambda x: x, reverse=True)
print(result)

words = ["cat", "dog", "apple", "banana"]
result = sorted(words, key=lambda w: w[-1])
print(result)