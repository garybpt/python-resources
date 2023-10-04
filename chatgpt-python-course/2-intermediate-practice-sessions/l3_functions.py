# Define a function called calculate_sum that takes two parameters, sum1 and sum2.
def calculate_sum(sum1, sum2):
    # Inside the function, add sum1 and sum2 and return the result.
    return sum1 + sum2

# Ask the user for the first value and store it in the sum1 variable.
sum1 = input("What is the first value? ")
# Convert the user's input (a string) into an integer.
sum1 = int(sum1)

# Ask the user for the second value and store it in the sum2 variable.
sum2 = input("What is the second value? ")
# Convert the user's input (a string) into an integer.
sum2 = int(sum2)

# Call the calculate_sum function with the user's input values and store the result in the total variable.
total = calculate_sum(sum1, sum2)

# Display the result to the user.
print("The total is:", total)