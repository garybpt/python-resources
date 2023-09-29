numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Create a new list 'first_half' containing the first half of the numbers

first_half = numbers[:3]
print(first_half)

# Create a new list 'last_three' containing the last three numbers

last_three = numbers[6:]
print(last_three)

# Create a new list 'even_numbers' containing every second number, starting from the second number in the list

even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)