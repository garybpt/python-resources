spam = {'name': 'Zophie', 'age': 7}

if 'name' in spam.keys():
    print('True')
else:
    print('False')

if 'Zophie' in spam.values():
    print('True')
else:
    print('False')

if 'colour' in spam.keys():
    print('True')
else:
    print('False')

if 'colour' not in spam.keys():
    print('True')
else:
    print('False')

if 'colour' in spam:
    print('True')
else:
    print('False')