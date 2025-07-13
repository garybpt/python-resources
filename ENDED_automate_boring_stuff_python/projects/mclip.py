#! Python3
# mclip.py - This is a project that saves multiple items to the clipboard

import sys
import pyperclip

TEXT = {'agree': """Yes, I agree. That sounds good to me.""",
        'busy': """Sorry, can we do this later?""",
        'upsell': """Would you consider setting up a monthly donation?"""}

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] # First command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to the clipboard')
else:
    print('There is no text for ' + keyphrase)