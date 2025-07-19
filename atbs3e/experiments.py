print('Please input any number.')
num = int(input(''))

if num >= 100:
    print('That is 100 or greater')
elif num >= 50:
    print('Within 50-99 range.')
elif num >= 10:
    print('Within 10-49 range.')
else:
    print('That is 9 or less')