# The ord() and chr() functions

spam = ord('A') # Converts 'A' into its Unicode code point
print(spam) # 65

spam = ord('4') # Converts '4' (string) into its Unicode code point
print(spam) # 52

spam = ord('!')  # Converts '!' into its Unicode code point
print(spam) # 33

spam = chr(65)  # Converts 'A' (integer) into its Unicode code point
print(spam) # A

spam = ord('B')
print(spam)

spam = ord('A') < ord('B')
print(spam)

spam = chr(ord('A'))
print(spam)

spam = chr(ord('A') + 1)
print(spam)