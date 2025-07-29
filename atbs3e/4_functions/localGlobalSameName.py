# Global variable (outside functions) and local variables (inside functions) can have the same name but its best avoided

def spam():
    eggs = 'spam local'
    print(eggs) # Prints 'spam local'

def bacon():
    eggs = 'local bacon'
    print(eggs) # Prints 'local bacon'
    spam()
    print(eggs) # Prints 'bacon local'

eggs = 'global'
bacon()
print(eggs) # Prints 'global'