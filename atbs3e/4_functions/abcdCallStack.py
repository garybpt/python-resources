# Python remembers where in code a function call is made, and returns there once the function's purpose is complete

def a():
    print('a() starts')
    b() # a() immediately calls b()
    d() # a() calls d()
    print('a() returns') # a() prints that it returns, which is its end, and returns to the a() function call

def b():
    print('b() starts')
    c() # b immideiately called c()
    print('b() returns') # b() doesn't call anything either, so the programme returns to a()

def c():
    print('c() starts') # c() doesn't call anything, so the programme returns to b()
    print('c() returns')

def d():
    print('d() starts') # d() doesn't call anything, so again, the programme returns to a()
    print('d() returns')

a() # a() is called first