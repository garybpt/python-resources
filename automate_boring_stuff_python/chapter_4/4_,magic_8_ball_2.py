import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

question = input("What would you like to predict? ") # Added this question in for practice

print(question + ' ' + messages[random.randint(0, len(messages) - 1)]) # Added 'question' and ' ' in for practice