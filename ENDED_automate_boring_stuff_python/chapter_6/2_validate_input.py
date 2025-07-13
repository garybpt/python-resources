# This programme repeatedly asks the user for their age and a password until they provide valie input

while True: # Ask the user for their age
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        break # If age is a valid decimal then we break out of this while loop
    print('Please enter a number for your age.')

while True: # Ask the user for a password
    print('Select a new password (letters and numbers only): ')
    password = input()
    if password.isalnum():
        break # If the password is letters and numbers we break out of the while loop
    print('Passwords can only have letters and numbers.')