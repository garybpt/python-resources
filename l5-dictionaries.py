# Creating an empty dictionary
my_dict = {}

# Creating a dictionary for a book
book = {
    "author": "Christopher McDougall",
    "title": "Born to Run",
    "year": 2008
}

# Updating the year and adding a new key for genre
book["year"] = 2009
book["genre"] = "Adventure"

# Looping through the keys and values of the book dictionary
for key, value in book.items():
    print(key, value)