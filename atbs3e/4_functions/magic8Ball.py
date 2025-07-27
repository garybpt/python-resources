import random

def get_answer(answer_number):
    # Returns a fortune answer based on what int answer_number is, 1-9
    if answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'It is decidedly so'
    elif answer_number == 3:
        return 'Yes'
    elif answer_number == 4:
        return 'Reply hazy, try again'
    elif answer_number == 5:
        return 'Ask again later'
    elif answer_number == 6:
        return 'Concentrate and ask again'
    elif answer_number == 7:
        return 'Outlook not so good'
    elif answer_number == 8:
        return 'Very doubteful'
    
print('Ask a yes or no question:')
input('>')
r = random.randint(1, 9) # Picks a random integer between 1-8
fortune = get_answer(r) # Random integer gets assigned to r which is then passed to the function
print(fortune) # Assigned number is given a string, which is then assigned to fortune, and then printed


# Alternate function call
# print(get_answer(random.randint(1, 9)))