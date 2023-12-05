try:
    # Attempt to perform division
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2

except ZeroDivisionError:
    # Handle the ZeroDivisionError exception
    print("Error: Division by zero!")

except ValueError:
    print("Error: Invalid input! Please enter a numeric value.")

else:
    # Code in the 'else' block executes if no exception occurred
    print(f"Result: {result:.2f}")

finally:
    # The 'finally' block always executes, regardless of exceptions
    print("Program finished execution.")