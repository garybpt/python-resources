# Starting list of numbers
numbers = [1, 2, 3, 4, 5]

# Append 6 to the end of the list
numbers.append(6)
print(numbers)

# Insert 0 at the beginning of the list
numbers.insert(0, 0) # First 0 is position, second 0 is the number being listered
print(numbers)

# Remove 3 from the list
numbers.remove(3)
print(numbers)

# Extend the list with 7, 8, and 9
numbers.extend([7, 8, 9]) # Note the brackets because we are adding another list to the end
print(numbers)

# Sort the list in ascending order
numbers.sort()
print(numbers)

# Sort the list in descending order
numbers.reverse()
print(numbers)