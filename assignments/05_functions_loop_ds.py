menu = {
    1: {"name": 'espresso', "price": 1.99},
    2: {"name": 'coffee', "price": 2.50},
    3: {"name": 'cake', "price": 2.79},
    4: {"name": 'soup', "price": 4.50},
    5: {"name": 'sandwich', "price": 4.99}
}

"""
Calculates the subtotal of an order.
        1. Add up the prices of all items in the order.
        2. Round the result to 2 decimal places and return it.
    Args:
        order (list): A list of dicts, where each dict represents an item with a name and price.
    Returns:
        float: The subtotal of all item prices, rounded to 2 decimal places.
"""
def calculate_subtotal(order:list):
    print('Calculating bill subtotal...')

    subtotal = 0
    for item in order:
        subtotal += item['price']
    return round(subtotal, 2)
    
"""
Calculates the tax of an order.
        1. Calculate 15% of the subtotal.
        2. Round the tax to 2 decimal places and return it.
    Args:
        subtotal (float): The subtotal amount.
    Returns:
        float: The calculated tax amount, rounded to 2 decimal places.
"""
def calculate_tax(subtotal):
    return round((subtotal * 15) / 100, 2)

"""
Summarizes the order.
        1. Calculate subtotal and tax.
        2. Compute the total (subtotal + tax) and round to 2 decimal places.
        3. Extract the item names and return them with the total.
    Args:
        order (list): A list of dicts, where each dict represents an item with a name and price.
    Returns:
        tuple: A list of item names and the total amount (rounded to 2 decimal places).
"""
def summarize_order(order):
    print_order(order)

    names = [item["name"] for item in order]

    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    total_amount = subtotal + tax

    return names, round(total_amount, 2)


# This function is provided for you and will print out the items in an order
def print_order(order):
    print("You have ordered " + str(len(order)) + " items")
    items = [item["name"] for item in order]
    print(items)
    return order

# This function is provided for you and will display the menu
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()


# This function is provided for you and will create an order by prompting the user to select menu items
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order

def main():
    order = take_order()
    print_order(order)
    
    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

    tax = calculate_tax(subtotal)
    print(f"Tax for the order is: {tax}")

    names, total = summarize_order(order)
    print(f"Order summary: Items: {names}, Total: {total}")

    

if __name__ == "__main__":
    main()