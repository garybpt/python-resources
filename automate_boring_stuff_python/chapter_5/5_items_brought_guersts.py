# A programme that tells you how many items guests are bringing.

all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
              'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}}

def total_brought(guests, item):
    num_brought = 0
    # Inside the total_brought() function, the for loop iterates over the key-value pairs in guests
    for k, v in guests.items():
        # Inside the loop, the string of the guest’s name is assigned to k, and the dictionary of picnic items they’re bringing is assigned to v. If the item parameter exists as a key in this dictionary, its value (the quantity) is added to num_brought
        num_brought = num_brought + v.get(item, 0)
    return num_brought
    
print('Number of things being brought')
print('- Apples:          ' + str(total_brought(all_guests, 'apples')))
print('- Cups:            ' + str(total_brought(all_guests, 'cups')))
print('- Cakes:           ' + str(total_brought(all_guests, 'cakes')))
print('- Ham Sandwiches:  ' + str(total_brought(all_guests, 'ham sandwiches')))
print('- Apple Pies:      ' + str(total_brought(all_guests, 'apple pies')))