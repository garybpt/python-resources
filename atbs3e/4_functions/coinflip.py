import random

h_count = 0 # PRACTICE: This is an addition to test my knowledge. The count for each coin side starts at 0
t_count = 0

for i in range(100): # Perform 100 coin flips
    if random.randint(0, 1) == 0:
        h_count = h_count + 1 # PRACTICE: For every flip of H/T a score is added
        print('H', end=' ') # Replaces a new line with a space
    else:
        t_count = t_count + 1
        print('T', end=' ')
print() # Print one new line at the end

print('H = ' + str(h_count)) # PRACTICE: Printing the total number of H/T scores
print('T = ' + str(t_count))