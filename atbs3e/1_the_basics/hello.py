# This programme says 'hello' and asks for your name

print('Hello, world!")')
print('What is your name?')

my_name = input('>')

print('It is good to meet you meet you, ' + my_name)
print('The length of your name is:')
print(len(my_name))
print('What is your age?')

my_age = input('>')

print('You will be ' + str(int(my_age) + 1) + ' in a year.')
# Take my_age as a string, converts it to an integer, adds 1, then converts it back to a string.