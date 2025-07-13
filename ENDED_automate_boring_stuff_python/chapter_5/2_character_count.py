# This script counts the number of each character in the 'message' string.

message = 'It was a bright cold day in April, and the clocks were striking thirteen'

count = {}

for character in message:
    # The setdefault() method call ensures that the key is in the count dictionary (with a default value of 0) so the program doesn’t throw a KeyError error when count[character] = count[character] + 1 is executed
    count.setdefault(character, 0)

    count[character] = count[character] + 1

print(count)

# This section is an additional practice section where I count the length of the string

print('This string is ' + str(len(message)) + ' characters long.') # Remember to turn the integer into a string so that it can be concatenated


# An extra practice session using the above to count the character in my name

print('What is your name?')
name = input()

identity = {}

for x in name:
    identity.setdefault(x, 0)

    identity[x] = identity[x] + 1

print(identity)

print('This name is ' + str(len(name)) + ' characters long.')