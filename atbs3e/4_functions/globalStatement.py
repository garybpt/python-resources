def spam():
    global eggs # Sets this function to the global variable when called
    eggs = 'spam'

eggs = 'global' # When the function spam() is called, this variable is overridden
spam()
print(eggs) # Prints 'spam'