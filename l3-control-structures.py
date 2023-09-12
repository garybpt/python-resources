# Ask the user for their age
age = input("How old are you? ")
age = int(age)  # Convert the input to an integer

# Determine if they are a child, teenager, or adult
if age < 18:
    print("You are a youngling")
elif age == 18:
    print("You are 18")
else:
    print("You're knocking on a bit")

# Use a loop to print numbers from 1 to 10
count = 1

while count <= 10:
    print(count)
    count += 1

# Create a function to add two numbers
def add_numbers(num1, num2):
    result = num1 + num2
    return result

# Call the function with two numbers and print the sum
num1 = 10
num2 = 10
sum_result = add_numbers(num1, num2)
print("The sum is:", sum_result)