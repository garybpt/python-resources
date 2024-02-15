#! Python3
# pig_latin.py - Changes English to Pig Latin

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

print('Enter the English message to translate into Pig Latin: ')
message = input()

pig_latin = [] # A list of the words in Pig Latin
for word in message.split():
    # Separate the non-letters at the start of this word
    prefix_non_letters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letters += word[0]
        word = word[1:]
    if len(word) == 0:
        pig_latin.append(prefix_non_letters)
        continue

    # Separate the non-letters at the end of this word
    suffix_non_letters = ''
    while not word[-1].isalpha():
        suffix_non_letters = word[-1] + suffix_non_letters
        word = word[:-1]
    
    # Remember if the word was in uppercase of title case
    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower() # Make the word lower case for transalation

    # Separate the consonants at the start of this word
    prefix_consonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefix_consonants += word[0]
        word = word[1:]

    # Add the Pig Latin ending to the word
    if prefix_consonants != '':
        word += prefix_consonants + 'ay'
    else:
        word += 'yay'
    
    # Set the word back to uppercase or title case
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()
    
    # Add the non-letters back to the start of the word
    pig_latin.append(prefix_non_letters + word + suffix_non_letters)

# Join all the words back together into a single string
print(' '.join(pig_latin))