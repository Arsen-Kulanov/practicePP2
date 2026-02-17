numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

nums = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)

words = ["cat", "elephant", "dog", "tiger"]
result = list(filter(lambda w: len(w) > 4, words))
print(result)

nums = [-3, -1, 0, 2, 5]
result = list(filter(lambda x: x > 0, nums))
print(result)

names = ["Arsen", "Bob", "Anna", "Mike"]
result = list(filter(lambda name: name.startswith("A"), names))
print(result)