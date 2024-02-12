# In this program, we define a printPicnic() method that will take in a dictionary of information and use center(), ljust(), and rjust() to display that information in a neatly aligned table-like format

def print_picnic(items_dict, left_width, right_width):
    print('PICNIC ITEMS'.center(left_width + right_width, '-'))
    for k, v in items_dict.items():
        print(k.ljust(left_width, '.') + str(v).rjust(right_width))

picnic_items = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

print_picnic(picnic_items, 12, 5) # First define the list, second define the leff padding, third define the right padding
print_picnic(picnic_items, 20, 6)