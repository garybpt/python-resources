def spam():
    global eggs
    eggs = 'spam' # This is the global variable

def bacon():
    eggs = 'bacon' # This is the local variable

def ham():
    print(eggs) # This is the global variable

eggs = 'global' # This is the global variable
spam()
print(eggs)