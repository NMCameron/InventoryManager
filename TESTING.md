# Inventory Manager Testing

| # | Feature | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|
| 1 | Missing inventory file | Start program without inventory.txt | Start with an empty inventory without crashing | Program displayed error and started with an empty inventory. | Pass |
| 2 | View empty inventory | Select view inventory with no items | Displays "No inventory items found." | Program displayed correct error | Pass |
| 3 | Add valid item | Enter a valid name, category, and quantity | Item is added and saved | Item was added successfully and saved to inventory.txt | Pass |
| 4 | Empty item name | Enter an empty item name | Empty name is rejected | Program displayed error and rejected the empty name | Pass |
| 5 | Duplicate item name | Enter an existing item name with different capitalization | Duplicate item is rejected | Program displayed error and rejected the duplicate. | Pass |
| 6 | Nonnumeric quantity | Enter "abc" as quantity | Nonnumeric quantity is rejected | Program rejected the quantity. | Pass |
| 7 | Negative quantity | Enter -5 as quantity | Negative quantity is rejected | Program rejected the quantity. | Pass |
| 8 | Update valid item | Select an item and enter a new quantity | Item quantity is updated | Item quantity was updated | Pass |
| 9 | Invalid item number | Enter a number outside range | rejected without crashing | Correct error displayed and returns | Pass |
| 10 | Remove item | Select an existing item to remove | Item is removed from inventory | Removed and updated inventory | Pass |
| 11 | Case-insensitive partial search | Search "ChAr" when inventory contains "Laptop Charger" and "Phone Charger" | Matching items are displayed | Program displayed "Laptop Charger" and "Phone Charger" | Pass |
| 12 | Search with no matches | Search for an item that does not exist | Displays "No inventory items matched your search." | Correct error thrown | Pass |
| 13 | Inventory summary | Display summary with items in multiple categories | Displays correct unique items, total quantity, low-stock items, and category counts | Program displayed the inventory totals, low-stock count, and category counts correctly. | Pass |
| 14 | Inventory persistence | Add an item, close the program, then restart | Previously saved inventory is loaded | Inventory persists across restarts. | Pass |