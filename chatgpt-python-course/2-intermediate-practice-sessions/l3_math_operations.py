# Import the calculate_sum function from the l3_functions module.
from l3_functions import calculate_sum

# Ask the user for the first number and store it in the sum1 variable.
sum1 = input("Enter the first number: ")
# Convert the user's input (a string) into an integer.
sum1 = int(sum1)

# Ask the user for the second number and store it in the sum2 variable.
sum2 = input("Enter the second number: ")
# Convert the user's input (a string) into an integer.
sum2 = int(sum2)

# Call the calculate_sum function with the user's input values and store the result in the total variable.
total = calculate_sum(sum1, sum2)

# Display the total, which contains the result of the calculation, to the user.
print("The total is:", total)