# An inventory management script after picking up loot


inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items(): # Loop through each item in the inventory
        print(str(v) + ' ' + k) # Print the quantity and name of each item
        item_total += v  # Incrementing the item_total by the quantity of each item
    print('Total number of items: ' + str(item_total))

def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1  # Increment the count in the inventory dictionary
        else:
            inventory[item] = 1   # Add the item to the inventory with count 1 if it doesn't exist
    return inventory  # Return the updated inventory
    

inv = add_to_inventory(inv, dragon_loot)

display_inventory(inv)