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


def add_item(inventory):
    """Add a new inventory item after validating user input"""
    name = input("Enter the item name: ").strip()

    if not name:
        print("Item name cannot be empty.")
        return
    
    if "|" in name:
        print("Item name cant contain the | character.")
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

    new_item = {
        "name": name,
        "category": category,
        "quantity": quantity
    }
        
    inventory.append(new_item)

    print("Item added successfully.")
    save_inventory(inventory, INVENTORY_FILE)



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
            
        elif choice == "7":
            print("Thank you for using Inventory Manager!")
            break
        elif choice in ["3", "4", "5", "6"]:
            print("This feature has not been implemented yet.")
        else:
            print("Invalid option. please put a valid number.")


if __name__ == "__main__":
    main()

