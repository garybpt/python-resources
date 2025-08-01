import random

random_number = random.randint(1,6)

def get_random_dice_roll(): # Returns a random integer from 1 to 6
    return random_number

print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())

# This script always prints the same number.
# The reason why this happens is because the random number is called at the beginning of the script, and is only called once.
# To fix this, the random number call should be called within the function using 'return random.randint(1, 6)'