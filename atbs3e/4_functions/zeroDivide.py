def spam(divide_by):
    try: # Any code in this block that causes ZeroDivisionError won't crash the programme
        return 42 / divide_by
    except ZeroDivisionError: # If ZeroDivisionError occurs, the code in this block runs
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0)) # You cannot divide a number by 0
print(spam(1))