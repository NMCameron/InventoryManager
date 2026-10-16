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
    return inventory



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

    while True:        
        display_menu()
        choice = input("Choose an option: ").strip()
        
        if not choice.isdigit():
           print("Error: Please enter a number\n")
           continue
        else:
            choice = int(choice)

        if choice == 1:
            view_inventory(inventory)
        elif choice == 2:
            add_item()
        elif choice == 3:
            update_quantity()
        elif choice == 4:
            remove_item(inventory)
        elif choice == 5:
            search_inventory()
        elif choice == 6:
            view_inventory()
        elif choice == 7:
            print("Exiting...")
            return
        else:
            print("Please enter a valid menu option.")



if __name__ == "__main__":
    main()