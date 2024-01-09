# This is a guess the number game.

import random

print("Hello there! What is your name?")
name = input()

secret_number = random.randint(1, 20)
print("Hey, " + name + ". I'm thinking of a number between 1 and 20.")

# Ask the player to guess 5 times.
for guesses_taken in range(1, 6):
    print('Take a guess.')
    guess = int(input())

    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        break    # This condition is the correct guess!

if guess == secret_number:
    print("Good job, " + name + "! You guessed my number in " + str(guesses_taken) + " guesses!")
else:
    print("Nope. Sorry, " + name + "! The number I was thinking of was " + str(secret_number) + ".")