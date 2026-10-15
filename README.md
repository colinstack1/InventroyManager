# Inventory Manager

## Project Overview

Inventory Manager is a Python command-line application designed to help users organize, track, and manage inventory items. The application allows users to categorize inventory, track quantities, update stock levels, and search for specific items.

The program stores inventory records in a text file, allowing changes to remain saved after the application closes.

## Features

- View all inventory items in a numbered list.
- Add new items with a name, category, and quantity.
- Update the quantity of an existing item.
- Remove items from inventory.
- Search inventory using partial, case-insensitive item names.
- View inventory summaries including total quantities, unique items, low-stock items, and category counts.
- Validate user input to prevent invalid quantities, duplicate item names, and incorrect item selections.
- Automatically save changes to the inventory file.

## Requirements

- Python 3
- A computer running macOS, Windows, or Linux
- A terminal or command-line application
- No additional Python packages required

## Project Files

| File | Description |
|---|---|
| `inventory_manager.py` | Contains the application's Python functions and main menu. |
| `inventory.txt` | Stores inventory item names, categories, and quantities. |
| `README.md` | Provides project documentation and instructions. |
| `TESTING.md` | Records tests performed and their results. |
| `AI_USAGE.md` | Documents AI assistance used during development. |
| `.gitignore` | Prevents temporary and sensitive files from being tracked by Git. |

## Inventory Data Format

Inventory data is stored in `inventory.txt` using the following format:

`Name|Category|Quantity`

Example:

`Laptop|Computers|25`

Each inventory item occupies one line. The pipe character separates the name, category, and quantity. Quantities are stored as nonnegative whole numbers.

## Running the Program

The application was developed and tested using Python 3 and Visual Studio Code on macOS.

1. Download or clone the InventoryManager repository from GitHub.
2. Open the InventoryManager folder in Visual Studio Code.
3. Open a terminal in the project directory.
4. Run the command:

   `python3 inventory_manager.py`

5. Follow the menu prompts to manage inventory.

If `inventory.txt` does not exist, the program starts with an empty inventory.

## Menu Options

| Option | Function |
|---|---|
| 1 | View inventory |
| 2 | Add an item |
| 3 | Update an item quantity |
| 4 | Remove an item |
| 5 | Search inventory |
| 6 | View inventory summary |
| 7 | Exit |

## Sample Interaction

The following example demonstrates updating the quantity of an existing item:

```text
Choose an option: 3
Enter the item number to update: 1
Enter the new quantity: 25
Laptop quantity updated to 25.
```

The updated quantity is saved to `inventory.txt` and remains available when the program restarts.

## Testing Summary

The application was tested using valid and invalid inputs to verify inventory functionality, validation, file handling, and data persistence.

Testing included adding and removing items, updating quantities, rejecting invalid input, searching inventory, and checking inventory summaries.

Detailed test cases, expected outcomes, actual results, and pass/fail statuses are documented in `TESTING.md`.

## Git and GitHub Development

Git was used for version control throughout development, with meaningful commits documenting completed features.

The inventory search feature was developed on a separate branch named `feature/inventory-search`.

A GitHub issue was created to document the search requirements. The feature was tested, reviewed through a pull request, and merged into the `main` branch using a merge commit.

## Known Limitations

- The application runs in a terminal and does not include a graphical user interface.
- Inventory items are stored in a local text file rather than a database.
- Inventory information is limited to item names, categories, and quantities.
- Inventory searches currently match item names rather than categories.
- The application does not support simultaneous updates by multiple users.

## Possible Future Improvements

- Develop a graphical user interface.
- Add inventory sorting and filtering.
- Search inventory by category.
- Add low-stock alerts.
- Store inventory information in a database.
- Support multiple users and inventory locations.

## AI Assistance

AI assistance was used for programming explanations, debugging, code review, and testing guidance. Additional information about how AI was used and verified is available in `AI_USAGE.md`.
