# Write a for loop to print the numbers from 1 to 10

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)

# Write a while loop to calculate the sum of all even numbers from 1 to 20

count = 1  # Start from the first odd number
sum_even = 0

while count <= 20:
    if count % 2 == 0:
        sum_even += count
    count += 1

print("Sum of even numbers from 1 to 20:", sum_even)

# Write a for loop to print each character in a given string, one character per line

characters = ["A", "B", "C", "D", "E"]
for character in characters:
    print(character)