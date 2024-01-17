# A simple script to find out people's birthdays

# You can see if the entered name exists as a key in the dictionary with the in keyword
birthdays = {'Alice': 'April 1', 'Bob': 'December 12', 'Carol': 'March 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        # If the name is in the dictionary, you access the associated value using square brackets
        print(birthdays[name] + ' is the birthday of ' + name)

    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        # If not, you can add it using the same square bracket syntax combined with the assignment operator
        birthdays[name] = bday
        print('Birthday database updated')