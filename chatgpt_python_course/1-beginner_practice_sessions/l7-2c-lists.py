# Exercise 1: Generate a list of the first 10 positive even numbers (2, 4, 6, ...)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

# Exercise 2: Extract the vowels from a given string
statement = "My name is Gary Butterfield and I'm from Yorkshire"
vowels = ["a", "e", "i", "o", "u"]
vowel_list = []

for char in statement:
    if char.lower() in vowels:
        vowel_list.append(char)

# Now, vowel_list contains the extracted vowels
print("Extracted vowels:", vowel_list)

# "char" is not a set variable, it can be represented by whatever is desired (for example "c", "letter" etc.)