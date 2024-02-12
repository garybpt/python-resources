# The join(), split(), and partition() methods

list = (['cats', 'rats', 'bats']) # Returns a string seperated by ', '
output = ', '.join(list)
print(output)

list = (['My', 'name', 'is', 'Gary']) # Returns a string seperated by ' '
output = ' '.join(list)
print(output)

list = (['My', 'name', 'is', 'Gary']) # Returns a string seperated by 'ABC'
output = 'ABC'.join(list)
print(output)

output = 'My name is Gary'.split() # Returns a list split at spaces
print(output)

output = 'MyABCnameABCisABCGary'.split('ABC') # Returns a list split at 'ABC'
print(output)

output = 'My name is Gary'.split('m') # Returns a list split at 'm'
print(output)

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Expiriment.
Please do not drink it.
Sincerely,
Bob'''.split('\n') # Returns a list split at '\n'
print(spam)

spam = 'Hello, world!'.partition('w') # Seperates into 3 from 'w'
print(spam)

spam = 'Hello, world!'.partition('world') # Sperates into 3 from 'world'
print(spam)

spam = 'Hello, world!'.partition('o') # Seperates into 3 from the first 'o'
print(spam)

spam = 'Hello, world!'.partition('XYZ') # Returns the full string becasue 'XYZ' do not exist in the string
print(spam)

before, sep, after = 'Hello, world!'.partition(' ') # Specifies the three strings
print(before)
print(after)



# The rjust(), ljust(), and center() methods

spam = 'Hello'.rjust(10) # Pads the string right with spaces to 10 characters total
print(spam) # '     Hello'

spam = 'Hello'.rjust(20) # Pads the string right with spaces to 20 characters total
print(spam) # '               Hello'

spam = 'Hello, world'.rjust(20) # Pads the string right with spaces to 20 characters total
print(spam) # '        Hello, world'

spam = 'Hello'.ljust(10) # Pads the string left with spaces to 10 characters total
print(spam) # 'Hello     '

spam = 'Hello'.rjust(20, '*') # Pads the string right with stars to 20 characters total
print(spam) # '***************Hello'

spam = 'Hello'.ljust(20, '-') # Pads the string left with dashes to 20 characters total
print(spam) # 'Hello---------------'

spam = 'Hello'.center(20) # Pads the string to the centre with spaces to 20 characters total
print(spam) # '       Hello        '

spam = 'Hello'.center(20, '=') # Pads the string to the centre with equals signs to 20 characters total
print(spam) # '=======Hello========'



# The strip(), rstrip(), and lstrip() methds

spam = '     Hello, world     '.strip() # Strips all white space
print(spam) # 'Hello, world'

spam = '     Hello, world     '.lstrip() # Strips white space to the left of the string
print(spam) # 'Hello, world     '

spam = '     Hello, world     '.rstrip() # Strips white space the right of the string
print(spam) # '     Hello, world'

spam = 'SpamSpamBaconSpamEggsSpamSpam'.strip('ampS') # Removes a, m, p, S from the ends of the string - order of 'ampsS' doesn't matter
print(spam) # 'BaconSpamEggs'



# The ord() and chr() functions

spam = ord('A') # Converts 'A' into its Unicode code point
print(spam) # 65

spam = ord('4') # Converts '4' (string) into its Unicode code point
print(spam) # 52

spam = ord('!')  # Converts '!' into its Unicode code point
print(spam) # 33

spam = chr(65)  # Converts 'A' (integer) into its Unicode code point
print(spam) # A

spam = ord('B') # Converts 'B' into its Unicode code point
print(spam) # 66

spam = ord('A') < ord('B') # Works out whether 'A' (65) is less than 'B' (66)
print(spam) #True

spam = chr(ord('A')) # Gets the Unicode code value (ord()) then converts it back to a string (shr())
print(spam)

spam = chr(ord('A') + 1) # Add 1 to 'A' (65), whichs makes it equal 'B' (66)
print(spam) #'B'