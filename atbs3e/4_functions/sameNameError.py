def spam():
    print(eggs) # ERROR !
    eggs = 'spam local'

eggs = 'global'
spam() # This presents an error because the local variable is assigned AFTER the print call