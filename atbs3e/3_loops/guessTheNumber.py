# This is a guess the number game

import random

secret_number = random.randint(1, 20) # The secret number is stored here when the programme is first started
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times
for guesses_taken in range(1,7): # This is counting from 1 - 6 after each guess
    print('Take a guess.')
    guess = int(input('>')) # This converts the string into an integer and stores it in the guess variable

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break # This condition is the secret number and ends the for loop

if guess == secret_number:
    print('Great job! You got it in ' + str(guesses_taken) + ' guesses!') # Both of these variables are converted back into strings
else:
    print('Nope. The number was ' + str(secret_number + '.'))