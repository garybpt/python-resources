# Create and empty list
my_list = [] # Lists use []

#  Add specified contents to the list
my_list.append("apple")
my_list.append(42)
my_list.append(3.14)
my_list.append("banana")
print(my_list)

# Create a tuple and try to change one of the elements
my_tuple = ("apple", 42, 3.14, "banana") # Tuples use ()

my_tuple.remove("apple")
print(my_tuple) # You are not able to remove items from tuples, only lists. To remove items, new tuples need to be created

# Create a list of numbers 1-10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a list of squared numbers
squares = [x**2 for x in numbers]
print(squares)