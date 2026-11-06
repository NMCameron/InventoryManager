import pytest
from inventory_manager import load_inventory, save_inventory



@pytest.fixture
def inventory():
    return [
        {"name": "Notebook", "category": "Office Supplies", "quantity": 10},
        {"name": "Notepad", "category": "Office Supplies", "quantity": 5},
        {"name": "Laptop", "category": "Electronics", "quantity": 3},
        {"name": "Mouse", "category": "Electronics", "quantity": 8}
    ]



def test_load_inventory_valid(tmp_path, inventory):
    # Arrange
    inventory_file = tmp_path / "inventory.txt"
    inventory_file.write_text(
        "Notebook|Office Supplies|10\n"
        "Notepad|Office Supplies|5\n"
        "Laptop|Electronics|3\n"
        "Mouse|Electronics|8\n"
    )

    expected = inventory

    # Act
    result = load_inventory(inventory_file)

    # Assert
    assert result == expected



def test_load_inventory_integer_quantity(tmp_path, inventory):
    # Arrange
    inventory_file = tmp_path / "inventory.txt"
    inventory_file.write_text("Notebook|Office Supplies|10\n")

    expected = inventory[0]["quantity"]

    # Act
    result = load_inventory(inventory_file)

    # Assert
    assert result[0]["quantity"] == expected
    assert isinstance(result[0]["quantity"], int)



def test_load_inventory_blank_lines(tmp_path, inventory):
    # Arrange
    inventory_file = tmp_path / "inventory.txt"
    inventory_file.write_text(
        "Notebook|Office Supplies|10\n"
        "\n"
        "\n"
        "\n"
        "Laptop|Electronics|3\n"
    )

    expected = [inventory[0], inventory[2]]

    # Act
    result = load_inventory(inventory_file)

    # Assert
    assert result == expected



def test_load_inventory_missing_file(tmp_path):
    # Arrange
    inventory_file = tmp_path / "missing.txt"
    expected = []

    # Act
    result = load_inventory(inventory_file)

    # Assert
    assert result == expected



def test_save_inventory_multiple_items(tmp_path, inventory):
    # Arrange
    inventory_file = tmp_path / "inventory.txt"

    expected = (
        "Notebook|Office Supplies|10\n"
        "Notepad|Office Supplies|5\n"
        "Laptop|Electronics|3\n"
        "Mouse|Electronics|8\n"
    )

    # Act
    save_inventory(inventory, inventory_file)

    # Assert
    assert inventory_file.read_text() == expected



def test_save_inventory_empty(tmp_path):
    # Arrange
    inventory_file = tmp_path / "inventory.txt"
    inventory = []
    expected = ""

    # Act
    save_inventory(inventory, inventory_file)

    # Assert
    assert inventory_file.exists()
    assert inventory_file.read_text() == expected



def test_save_load_round_trip(tmp_path, inventory):
    # Arrange
    inventory_file = tmp_path / "inventory.txt"
    expected = inventory

    # Act
    save_inventory(inventory, inventory_file)
    result = load_inventory(inventory_file)

    # Assert
    assert result == expected



def test_search_exact(inventory):
    # Arrange
    search = "Laptop"
    expected = [inventory[2]]

    # Act
    result = [
        item for item in inventory
        if search.lower() in item["name"].lower()
    ]

    # Assert
    assert result == expected



def test_search_partial(inventory):
    # Arrange
    search = "Lap"
    expected = [inventory[2]]

    # Act
    result = [
        item for item in inventory
        if search.lower() in item["name"].lower()
    ]

    # Assert
    assert result == expected



def test_search_case_insensitive(inventory):
    # Arrange
    search = "lApToP"
    expected = [inventory[2]]

    # Act
    result = [
        item for item in inventory
        if search.lower() in item["name"].lower()
    ]

    # Assert
    assert result == expected



def test_remove_first_item(inventory):
    # Arrange
    choice = 1
    expected = [inventory[1], inventory[2], inventory[3]]

    # Act
    inventory.pop(choice - 1)

    # Assert
    assert inventory == expected



def test_remove_last_item(inventory):
    # Arrange
    choice = 3
    expected = [inventory[0], inventory[1], inventory [3]]

    # Act
    inventory.pop(choice - 1)

    # Assert
    assert inventory == expected



def test_remove_negative_item(inventory):
    # Arrange
    choice = -1
    expected = inventory.copy()

    # Act
    if choice < 1 or choice > len(inventory):
        valid = False
    else:
        valid = True
        inventory.pop(choice - 1)

    # Assert
    assert valid is False
    assert inventory == expected