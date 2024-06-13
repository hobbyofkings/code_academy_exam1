# Validate price
# Objective: Write a function `has_valid_price` that checks if each product has a valid price. A valid price must be either an integer or a float, and greater than or equal to zero. Products with a price of 0 are considered free and count as valid.
# Parameters:
# - product: A dictionary containing product details with at least a 'price' key.
# Returns:
# - A Boolean value: True if the product has a valid price, False otherwise.
# Details:
# - If the price is not an integer or a float, return False.
# - If the price is less than zero, return False.
# - If the product is None or does not contain a 'price' key, return False.



def has_valid_price(product):
    if product is None or 'price' not in product:
        return False
    price = product['price']
    if not isinstance(price, (int, float)):
        return False
    if price < 0:
        return False
    return True

print(has_valid_price({ "product": "Milk", "price": 1.50 }))  # Expected: True
print(has_valid_price({ "product": "Cheese", "price": -1 }))  # Expected: False
print(has_valid_price({ "product": "Eggs", "price": 0 }))  # Expected: True
print(has_valid_price({ "product": "Cereals", "price": "3.0" }))  # Expected: False
print(has_valid_price(None))  # Expected: False


