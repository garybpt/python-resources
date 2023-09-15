try:
    result = 20 / 0  # Attempt to divide by zero
except ZeroDivisionError:
    print("There has been an error")  # Handle the ZeroDivisionError
finally:
    print("We always be runnin'")  # This always runs