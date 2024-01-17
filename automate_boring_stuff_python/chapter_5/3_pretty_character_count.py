# This script counts the number of each character in the 'message' string but in a prettier fashion using the pprint library. 

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen'

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# When the program is run, the output looks much cleaner, with the keys sorted
pprint.pprint(count)