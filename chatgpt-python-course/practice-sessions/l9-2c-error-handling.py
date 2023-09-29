num1 = input("What is your first number? ")
num1 = int(num1)

num2 = input("What is your second number? ")
num2 = int(num2)

try:
    result = num1 / num2 # Attempt to divide num1 by num2
    print(result)

except ZeroDivisionError:
    print("There was an error") # Handle the ZeroDivisionError