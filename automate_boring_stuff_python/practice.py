import copy

spam = ['A', 'B', 'C', 'D']

print(id(spam))

cheese = copy.copy(spam)

print(id(cheese)) # cheese is a different list with different identity

cheese[1] = 42

print(spam)

print(cheese)