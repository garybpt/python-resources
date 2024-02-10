spam = 'hello'

if spam.isalpha():
    print(True)
else:
    print(False)

spam = 'hello123'

if spam.isalpha():
    print(True)
else:
    print(False)

spam = 'hello123'

if spam.isalnum():
    print(True)
else:
    print(False)

spam = '123'

if spam.isdecimal():
    print(True)
else:
    print(False)

spam = '   '

if spam.isspace():
    print(True)
else:
    print(False)

spam = 'This Is Title Case'

if spam.istitle():
    print(True)
else:
    print(False)

spam = 'This Is Title Case 123'

if spam.istitle():
    print(True)
else:
    print(False)

spam = 'This Is not Title Case'

if spam.istitle():
    print(True)
else:
    print(False)

spam = 'This Is NOT Title Case Either'

if spam.istitle():
    print(True)
else:
    print(False)