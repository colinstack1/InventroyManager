"""
A Command line inventory management system

Author: Colin Stack
Course: CPS310
Assignment: Homework 1
"""

INVENTORY_FILE = "inventory.txt"

def display_menu():
    """ Display the menu to the user """
    print("\nInventory Management Menu")
    print("1. View inventory")
    print("2. Add an item")
    print("3. Update an item quantity")
    print("4. Remove an item")
    print("5. Search inventory")
    print("6. View inventory summary")
    print("7. Exit")

def load_inventory(filename):
    """ Load the inventory items from a text file into a list of dictionaries"""
    inventory = []

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                
                if not line:
                    continue

                name, category, quantity = line.split("|")

                item = {
                    "name": name,
                    "category": category,
                    "quantity": int(quantity)
                }
                inventory.append(item)
    except FileNotFoundError:
        return []
    
    return inventory

def save_inventory(inventory, filename):
    """ Save all the inventory items to a txt file"""
    with open(filename, "w") as file:
        for item in inventory:
            name = item["name"]
            category = item["category"]
            quantity = item["quantity"]

            file.write(f"{name}|{category}|{quantity}\n")


def view_inventory(inventory):
    """ Dsiplaying all the inventory items in a numbered list"""
    if not inventory:
        print("No inventory items found.")
        return
    
    print("\nInventory")

    for number, item in enumerate(inventory, start=1):
        print(f'{number}. {item["name"]} | {item["category"]} | Quantity: {item["quantity"]}')

def validate_new_item(inventory, name, category, quantity):
    """Validate a new inventory item and return an error or None."""
    name = name.strip()
    category = category.strip()

    if not name:
        return "Item name cannot be empty."

    if "|" in name:
        return "Item name cannot contain the | character."

    for item in inventory:
        if item["name"].lower() == name.lower():
            return "An item with that name already exists."

    if not category:
        return "Category cannot be empty."

    if "|" in category:
        return "Category cannot contain the | character."

    if not isinstance(quantity, int) or quantity < 0:
        return "Quantity must be a nonnegative whole number."

    return None



def add_item(inventory):
    """Add a new inventory item after validating user input."""
    name = input("Enter the item name: ").strip()

    if not name:
        print("Item name cannot be empty.")
        return

    if "|" in name:
        print("Item name cannot contain the | character.")
        return

    for item in inventory:
        if item["name"].lower() == name.lower():
            print("An item with that name already exists.")
            return

    category = input("Enter the category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    if "|" in category:
        print("Category cannot contain the | character.")
        return

    quantity_input = input("Enter the quantity: ").strip()

    if not quantity_input.isascii() or not quantity_input.isdecimal():
        print("Quantity must be a nonnegative whole number.")
        return

    quantity = int(quantity_input)

    validation_error = validate_new_item(
        inventory, name, category, quantity
    )

    if validation_error is not None:
        print(validation_error)
        return

    new_item = {
        "name": name,
        "category": category,
        "quantity": quantity,
    }

    inventory.append(new_item)

    print("Item added successfully.")
    save_inventory(inventory, INVENTORY_FILE)



def update_item_quantity(inventory, item_number, new_quantity):
    """Update an item's quantity using a one-based item number.

    Return True if successful, or False for invalid values.
    """
    if item_number < 1 or item_number > len(inventory):
        return False

    if not isinstance(new_quantity, int) or new_quantity < 0:
        return False

    inventory[item_number - 1]["quantity"] = new_quantity
    return True



def update_quantity(inventory):
    """Update the quantity of an existing inventory item."""
    if not inventory:
        print("No inventory item found.")
        return

    view_inventory(inventory)

    selection = input("Enter the item number to update: ").strip()

    if not selection.isascii() or not selection.isdecimal():
        print("Please enter a valid item number.")
        return

    item_number = int(selection)

    if item_number < 1 or item_number > len(inventory):
        print("That item number does not exist.")
        return

    quantity_input = input("Enter the new quantity: ").strip()

    if not quantity_input.isascii() or not quantity_input.isdecimal():
        print("Quantity must be a nonnegative whole number.")
        return

    new_quantity = int(quantity_input)

    updated = update_item_quantity(inventory, item_number, new_quantity)

    if updated:
        selected_item = inventory[item_number - 1]
        print(f'{selected_item["name"]} quantity updated to {new_quantity}.')
        save_inventory(inventory, INVENTORY_FILE)



def remove_item_by_number(inventory, item_number):
    """Remove an inventory item using a one-based item number.

    Return the removed item, or None if the number is invalid.
    """
    if item_number < 1 or item_number > len(inventory):
        return None

    return inventory.pop(item_number - 1)

def remove_item(inventory):
    """Remove an inventory item selected by the user."""
    if not inventory:
        print("No inventory item found.")
        return

    view_inventory(inventory)

    selection = input("Enter the item number to remove: ").strip()

    if not selection.isascii() or not selection.isdecimal():
        print("Please enter a valid item number.")
        return

    item_number = int(selection)

    removed_item = remove_item_by_number(inventory, item_number)

    if removed_item is None:
        print("That item number does not exist.")
        return

    print(f'Item removed: {removed_item["name"]}')
    save_inventory(inventory, INVENTORY_FILE)

def find_matching_items(inventory, search_term):
    """Return inventory items whose names match a search term."""
    search_term = search_term.strip()

    if not search_term:
        return[]
    
    matches = []

    for item in inventory:
        if search_term.lower() in item["name"].lower():
            matches.append(item)

    return matches


def search_inventory(inventory):
    """Search inventory by name and display matching items."""
    search_term = input("Enter an item name to search: ").strip()

    if not search_term:
        print("Search term cannot be empty.")
        return

    matches = find_matching_items(inventory, search_term)

    if not matches:
        print("No inventory items matched your search.")
        return

    print("\nSearch Results:")
    view_inventory(matches)


def display_summary(inventory):
    """Display inventory totals, low stock items, and category counts."""
    unique_items = len(inventory)
    total_quantity = 0
    low_stock_items = 0
    category_counts = {}

    for item in inventory:
        total_quantity += item["quantity"]

        if item["quantity"] < 5:
            low_stock_items += 1
        
        category = item["category"].strip()
        category_key = category.lower()

        if category_key not in category_counts:
            category_counts[category_key] = {
                "name": category,
                "count": 0
            }
        category_counts[category_key]["count"] += 1


    print("\nInventory Summary")
    print(f"Unique items: {unique_items}")
    print(f"Total quantity: {total_quantity}")
    print(f"Low-stock items: {low_stock_items}")

    print("\nItems by category: ")

    for category_info in category_counts.values():
        print(f'{category_info["name"]}: {category_info["count"]}')




def main():
    
    """ Run the inventory management system until the user chooses to exit """
    inventory = load_inventory(INVENTORY_FILE)

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            view_inventory(inventory)
        
        elif choice == "2":
            add_item(inventory)
        
        elif choice == "3":
            update_quantity(inventory)
            
        elif choice == "4":
            remove_item(inventory)

        elif choice == "5":
            search_inventory(inventory)
        
        elif choice == "6":
            display_summary(inventory)

        elif choice == "7":
            print("Thank you for using Inventory Manager!")
            break

        else:
            print("Invalid option. please put a valid number.")


if __name__ == "__main__":
    main()

