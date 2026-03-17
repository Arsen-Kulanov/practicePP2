# 1
x = map(len, ('apple', 'banana', 'cherry'))
print(list(x))

# 2
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
    if x < 18:
        return False
    else:
        return True

adults = filter(myFunc, ages)

for x in adults:
    print(x)

# 3
words = ["a", "apple", "banana", "b", " ", "cherry"]

def f(x):
    if len(x) > 1:
        return True
    else:
        return False
    
fruits = filter(f, words)
for i in fruits:
    print(i, end = " ")

# 4
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x * y, numbers)

print(result)

# 5
words = ["cat", "elephant", "dog", "hippopotamus"]

longest_word = reduce(lambda x, y: x if len(x) > len(y) else y, words)

print(longest_word)