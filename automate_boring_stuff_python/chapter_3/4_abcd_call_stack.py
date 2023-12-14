def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()

# This starts with a function call of a()
# This prints "a() starts"
# This then calls function b()
# b() prints "b() starts"
# b() then calls function c()
# c() calls nothing but prints "c() starts" and "c() returns" and goes back to b()
# b() prints "b() returns" and goes back to a()
# a() calls function d()
# d() calls nothing but prints "d() starts" and "d() returns" and goes back to a()
# a() prints "a() returns" and finished the programme. 