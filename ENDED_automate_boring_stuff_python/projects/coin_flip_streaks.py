# This is a coin flip script which predicts the likelihood of flipping a streak of 6


import random

def generate_coin_flips():
    # Generate a list of 100 'heads' or 'tails' values.
    return [random.choice(['heads', 'tails']) for _ in range(100)]

def has_streak(flips, streak_length):
    # Check if there is a streak of given length in a list.
    for i in range(len(flips) - streak_length + 1):
        # Check if the current sublist of length streak_length has all the same values.
        if all(flips[i + j] == flips[i] for j in range(streak_length - 1)):
            return True  # Return True if a streak is found.
    return False  # Return False if no streak is found.

numberOfStreaks = 0
for experimentNumber in range(10000):
    # Generate a list of 100 'heads' or 'tails'.
    flips = generate_coin_flips()
    
    # Check if there is a streak of 6 heads or tails in the list.
    if has_streak(flips, 6):
        numberOfStreaks += 1  # Increment the count if a streak is found.

# Print the percentage of experiments that resulted in a streak.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))