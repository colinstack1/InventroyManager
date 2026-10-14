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



def main():
    """ Run the inventory management system until the user chooses to exit """
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()
        
        if choice == "7":
            print("Thank you for using Inventory Manager!")
            break
        elif choice in ["1", "2", "3", "4", "5", "6"]:
            print("This feature has not been implemented yet.")
        else:
            print("Invalid option. please select a number from 1 to 7.")


if __name__ == "__main__":
    main()


#Temp testing (delete when done)
display_menu()