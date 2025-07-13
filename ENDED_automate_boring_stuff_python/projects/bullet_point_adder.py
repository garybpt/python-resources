#! Python3
# bullet_point_adder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard

import pyperclip

text = pyperclip.paste()

# Seperate lines and add stars
lines = text.split('\n')
for i in range(len(lines)): # Loop through the indexes for "lines" list
    lines[i] = '* ' + lines[i] # Add a star the each string in "lines" list

text = '\n'.join(lines)

pyperclip.copy(text)