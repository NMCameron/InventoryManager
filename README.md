# Inventory Manager

Inventory Manager is a command-line inventory management program.

It allows users to manage inventory items and track their quantities.

## Current Features

- Add, view, update, and remove inventory items.
- Search inventory by item name.
- View inventory summaries.
- Input validation.
- Persistent inventory storage.

## Requirements

- Python 3

## Project Files

- `inventory_manager.py` - Main program.
- `inventory.txt` - Stores inventory data.
- `TESTING.md` - Documents testing results.
- `.gitignore` - Specifies files Git should ignore.

## Inventory Data Format

Items are saved using `Name|Category|Quantity`.

Example:
```
Laptop Charger|Electronics|8
Phone Charger|Electronics|4
```

## Running the Program

Run on Windows in the terminal:
```
python inventory_manager.py
```
## Menu Options

1. View inventory
2. Add an item
3. Update an item quantity
4. Remove an item
5. Search inventory
6. View inventory summary
7. Exit

## Sample Interaction

Run the program using `python inventory_manager.py`  
Check your inventory by selecting "View inventory"  
Add a new item to inventory by selecting "Add an item"  
Update the quantity if needed  
Exit the program when you are finished  

## Testing Summary

The 14 required tests are documented in `TESTING.md`, covering inventory functions, invalid inputs, and data persistence.

## Version Control

This project uses Git locally and GitHub for version control, along with issues, branches, and pull requests.

## Known Limitations

- Inventory is stored locally in a text file.
- Only item quantities can be updated.

## Future Improvements

- Allow editing item names and categories.
- Add inventory sorting.
- Create a graphical interface.