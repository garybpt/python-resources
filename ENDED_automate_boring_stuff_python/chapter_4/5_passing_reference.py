def eggs(some_parameter):
    some_parameter.append('Hello') # Appends 'Hello' to the end of any list where the function is called
    some_parameter.reverse() # Added this in for practice - it will reverse the list

spam = [1, 2, 3]

eggs(spam) # The 'eggs' function call is using the 'spam' list and therefore appends 'Hello' to the end of it

print(spam)