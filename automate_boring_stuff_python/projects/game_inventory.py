# A script to manage a player's game inventory

player_inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items(): # Loop through each item in the inventory
        print(str(v) + ' ' + k) # Print the quantity and name of each item
        item_total += v  # Incrementing the item_total by the quantity of each item
    print('Total number of items: ' + str(item_total))

display_inventory(player_inventory)