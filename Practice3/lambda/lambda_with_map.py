numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

numbers = [1, 2, 3, 4, 5]
plusone = list(map(lambda x: x + 1, numbers))
print(plusone)

nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**2, nums))
print(result)

strings = ["1", "2", "3", "4"]
result = list(map(lambda x: int(x), strings))
print(result)

words = ["apple", "banana", "kiwi"]
result = list(map(lambda w: len(w), words))
print(result)

a = [1, 2, 3]
b = [4, 5, 6]
result = list(map(lambda x, y: x + y, a, b))
print(result)