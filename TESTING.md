# Inventory Manager Testing


## Testing results 

| 1 | Missing inventory file | temp. rename 'inventory.txt', then start the program | Program starts with an empty inventory without crashing | [Program started normally without the file] | [Pass] |


| 2 | view empty inventory | call 'view_inventory([])' during a temp test | displays 'no inventory items found.' | [displayed "No inventory items found.'] | [Pass] | 


| 3 | Add a valid item | Choose 2; enter 'USB Hub', 'Electronic', '8' | Item is added successfully and saved | [program displayed 'Item added successfully.'; file contents after this specific action not separatly verified] | [Partly] |


| 4 | Reject empty item name | Choose2; leave name blank | Reject input and returns to menu | [Displayed 'Item name cant be empty.'] | [Pass] |


| 5 | Reject duplicate name | choose 2; enter 'laptop' when 'Laptpp' exists | Reject duplicate regardless of capitalization | [Displays 'An item with that name already exists.'] | [Pass] |


| 6 | Reject nonumeric quantity | Choose 2; enter 'USB Cable', 'Electronic', 'five' | Rejects quantity without adding item | [Displays 'Quantity must be a nonnegative whole number.'] | [Pass] |


| 7 | Reject negativequantity | choose 2; enter a unique item name, category, then '-3' | Rejects negative quantity | [Dispalyed 'quantity must be a nonnegative whole number.'] | [Pass] |


| 8 | Update valid item quantity | Choose 3; select an existing item and enter a new nonnegative quantity | Updates the selected item and saves the changes to 25| [Displayed 'laptop quantity updated to 25] | [Pass] | 


| 9 | Reject invalid item number | choose 3; enter '999' | Displays an error and makes no change | [Displayed 'That item number does not exist.'] | [Pass] | 


| 10 | Remove an item | Choose 4; select an existing item number 10 (Test Removal)| Removes the selected item and saves the change | [Dispalyed confirmation; item disappeared rom inventory] | [Pass] |


| 11| Case-insesitive partial search | choose 5; search 'LAP' with 'Laptop' in inventory | Displays matching laptop items | [Laptop appeard in search result] | [Pass] | 


| 12 | Search with no matches | Choose 5; search 'nonexisting-item-xyz' | Dispalys 'No inventory matches your search.' | [displayed "no inventory items matched your search."] | [Pass] | 


| 13 | Inventory summary | choose 6 with the nine-item inventory | displays item count, total quantity, low stock count, and category counts | [display 9 unique items, total quantity 70, low stock items 2, categories computers 1, displays 1, accessories 2, printers 1, electronic 4. Category counts sum to 9; quantites not independently checked against file] | [Failed at first, then fixed errors to get a Pass] |


| 14 | File persistence | Successfully add or update an item, exit with 7, restart, and view inventory | Saved change remains after restart | [laptop still had quantity of 25 after restart] | [Pass] |


| 15 | Reject pipe in category | Choose 2; enter 'Webcam', then 'Office/Electronics' as category | Rejects the category | Displayed 'Category cannot contain the '|' character.' | [Pass] |


| 16 | Reject empty quantity | choose 2; enter 'Headset', 'Electronic', then blank quantity | Rejects empty quantity | [displayed 'quantity must be a nonnegative whole number.'] | [Pass] |


| 17 | Reject whitespace-only search  | choose 5; enter only spaces  | Rejects empty search term and returns to menu | [displayed 'search term cannot be empty.'] | [Pass] | 

## Testing env.
- OS: macOS
- Programming lang.: Python3
- Application entry point: 'python3 inventory_manager.py'
- Test method: manual command-line input and inspection of inventory.txt
