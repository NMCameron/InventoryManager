""""
Name: Cameron Nebel
Course: CPS 310
Project: Inventory manager - Emulate the needs of a small company and their inventory management system.
"""
INVENTORY_FILE = "inventory.txt"


def display_menu():
    """Displays menu options for user to choose from"""
    print("Inventory Manager\n\n" \
    "1. View inventory\n" \
    "2. Add an item\n" \
    "3. Update an item quantity\n" \
    "4. Remove an item\n" \
    "5. Search inventory\n" \
    "6. View inventory summary\n" \
    "7. Exit\n")



def load_inventory(INVENTORY_FILE):
    """"Loads inventory from file, creating an empty list if file not found"""
    inventory = []

    try:
        with open(INVENTORY_FILE, "r") as file:
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
        print("Inventory file not found.")
        return []

    return inventory



def save_inventory(inventory, INVENTORY_FILE):
    """Saves inventory to file and properly formats it"""
    with open(INVENTORY_FILE, "w") as file:
        for item in inventory:
            file.write(
                f"{item["name"]} | {item["category"]} | {item["quantity"]}\n"
                )



def view_inventory(inventory):
    """Iterates through every item in the inventory displaying it along with its name"""
    if not inventory:
            print("No inventory items found.")
            return
        
    print("Inventory:")
    for i, item in enumerate(inventory, start=1):
            print(f"{i}. {item["name"]}|{item["category"]}|Quantity: {item["quantity"]}")



def add_item(inventory):
    while True:
        name = input("Enter the item name: ").strip()

        if not name:
            print("Error: Name cannot be empty.")
        elif "|" in name:
            print("Error: Name can not contain '|'.")
        elif any(item["name"].lower() == name.lower() for item in inventory):
            print("Error: Item already exists.")
        else:
            break

    while True:
        category = input("Enter the category: ").strip()

        if not category:
            print("Error: Category cannot be empty.")
        elif "|" in category:
            print("Error: Category cannot contain '|'.")
        else:
            break

    while True:
        quantity = input("Enter the quantity: ").strip()

        if not quantity.isdigit():
            print("Quantity must be a nonnegative whole number.")
        else:
            quantity = int(quantity)
            break

    item = {
        "name": name,
        "category": category,
        "quantity": quantity
    }

    inventory.append(item)
    print("Item added successfully.")



def update_quantity(inventory):

    if not inventory:
        print("No inventory items found.")
        return

    view_inventory(inventory)

    choice = input("Enter the item number to update: ").strip()

    if not choice.isdigit():
        print("Error: Please enter a valid item number.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(inventory):
        print("Error: Please choose a valid item.")
        return

    quantity = input("Enter the new quantity: ").strip()

    if not quantity.isdigit():
        print("Quantity must be a nonnegative whole number.")
        return

    quantity = int(quantity)

    item = inventory[choice - 1]
    item["quantity"] = quantity

    print(f"{item['name']} quantity updated to {quantity}.")


def remove_item(inventory):

    if not inventory:
        print("No inventory items found.")
        return

    view_inventory(inventory)

    choice = input("Enter the item number to remove: ").strip()

    if not choice.isdigit():
        print("Error: Please enter a valid item number.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(inventory):
        print("Error: Please choose a valid item.")
        return

    removed_item = inventory.pop(choice - 1)

    print(f"Item removed: {removed_item['name']}")

    return



def search_inventory(inventory):
    search = input("Enter item name to search: ").strip()

    if not search:
        print("Error: Search cannot be empty.")
        return

    matches = []

    for item in inventory:
        if search.lower() in item["name"].lower():
            matches.append(item)

    if not matches:
        print("No inventory items matched your search.")
        return

    print("Search Results:")

    for index, item in enumerate(matches, start=1):
        print(f"{index}. {item['name']} | {item['category']} | Quantity: {item['quantity']}")



def display_summary(inventory):
    unique_items = len(inventory)
    total_quantity = 0
    low_stock = 0
    categories = {}

    for item in inventory:
        total_quantity += item["quantity"]

        if item["quantity"] < 5:
            low_stock += 1

        category = item["category"].lower()

        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1

    print("Inventory Summary")
    print(f"Unique items: {unique_items}")
    print(f"Total quantity: {total_quantity}")
    print(f"Low-stock items: {low_stock}")

    print("\nItems by category:")

    for category, count in categories.items():
        print(f"{category.title()}: {count}")



def main():
    #TODO set up main function, that controls everything
    inventory = load_inventory(INVENTORY_FILE)

    while True:        
        display_menu()
        choice = input("Choose an option: ").strip()
        
        if not choice.isdigit():
           print("Error: Please enter a number.\n")
           continue
        else:
            choice = int(choice)

        if choice == 1:
            view_inventory(inventory)
        elif choice == 2:
            add_item(inventory)
            save_inventory(inventory,INVENTORY_FILE)
        elif choice == 3:
            update_quantity(inventory)
            save_inventory(inventory, INVENTORY_FILE)
        elif choice == 4:
            remove_item(inventory)
            save_inventory(inventory,INVENTORY_FILE)
        elif choice == 5:
            search_inventory(inventory)
        elif choice == 6:
            display_summary(inventory)
        elif choice == 7:
            print("Exiting...")
            return
        else:
            print("Error: Please enter a valid menu option.\n")



if __name__ == "__main__":
    main()