INVENTORY_FILE = "inventory.txt"

def display_menu():
    #TODO: display menus
    print("Inventory Manager\n\n" \
    "1. View inventory\n" \
    "2. Add an item\n" \
    "3. Update an item quantity\n" \
    "4. Remove an item\n" \
    "5. Search inventory\n" \
    "6. View inventory summary\n" \
    "7. Exit\n")

def load_inventory(INVENTORY_FILE):
    #TODO read in inventory from file
    print("load inventory")
    with open (INVENTORY_FILE, "r") as file:
        inventory = file.read()




def save_inventory(inventory, INVENTORY_FILE):
    #TODO save inventory to text file
    print("save inventory")

def view_inventory(inventory):
    #TODO display inventory
    print("view inventory")

def add_item(inventory):
    #TODO add item to inventory
    print("add item")

def update_quantity(inventory):
    #TODO update quantity of inventory
    print("update quantity")

def remove_item(inventory):
    #TODO remove items from inventory
    print("remove item")

def search_inventory(inventory):
    #TODO search through inventory
    print("search inventory")

def display_summary(inventory):
    #TODO print item, category, and quantity
    print("display summary")

def main():
    #TODO set up main function, that controls everything
    load_inventory(INVENTORY_FILE)
    display_menu()

    menu_selection = input()
    menu_selection = int(menu_selection)
        
    if menu_selection == 1:
        view_inventory()
    elif menu_selection == 2:
        add_item()
    elif menu_selection == 3:
        update_quantity()
    elif menu_selection == 4:
        remove_item()
    elif menu_selection == 5:
        search_inventory()
    elif menu_selection == 6:
        view_inventory()
    elif menu_selection == 7:
        print("Exiting...")
        return
    else:
        print("Please enter a valid menu option.")
    
if __name__ == "__main__":
    main()