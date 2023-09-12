import math

# Function to calculate the factorial of a number using recursion
def num_factorial(n):
    if n == 0:
        return 1  # Base case: 0! is 1
    else:
        return n * num_factorial(n - 1)

# Calculate the factorial of 20 and print the result
result = num_factorial(20)
print("Factorial of 20 is: ", result)

# Function to generate a list of prime numbers within a specified range
def generate_prime_numbers(start, end):
    prime_numbers = []

    for num in range(start, end + 1):
        if num > 1:  # Prime numbers must be greater than 1
            is_prime = True
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)

    return prime_numbers

# Define the range for prime numbers (0 to 50)
start_range = 0
end_range = 50

# Generate and print prime numbers in the specified range
prime_list = generate_prime_numbers(start_range, end_range)
print("Prime numbers in the range", start_range, "to", end_range, "are:", prime_list)

# Define the range for the multiplication table (2 to 10)
start_num = 2
end_num = 10

# Loop to create and print a multiplication table
for i in range(start_num, end_num + 1):
    for j in range(start_num, end_num + 1):
        result = i * j
        print(i, "x", j, "=", result)