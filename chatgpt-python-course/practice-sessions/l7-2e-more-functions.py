def calculate_price(price, tax_rate, discount):
    return price + (price * tax_rate) - discount

total = calculate_price(price = 100, tax_rate = 0.2, discount = 0)

print("Totat: £", total)