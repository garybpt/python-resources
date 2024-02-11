while True:
    print('Please input a nickname. It must only contain letters.')
    nickname = input()
    if nickname.isalpha():
        break
    print('Please stick to the requirements.')

while True:
    print('Please input 3-5 random numbers.')
    numbers = input()
    if numbers.isdecimal():
        break
    print('Please stick to the requirements.')

print(f'Your password is: {nickname}{numbers}')
password = (nickname + numbers) # Something is going wrong here

while True:
    input('What is your password? ')
    question = input()
    if question == password:
        print('Access granted.')
    else:
        ('Access denied')