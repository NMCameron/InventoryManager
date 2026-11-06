from inventory_manager import load_inventory, save_inventory



def test_load_inventory_valid(tmp_path):
    # Arrange
    inventory_file = tmp_path / "inventory.txt"
    inventory_file.write_text(
        "Notebook|Office Supplies|10\n"
        "Laptop|Electronics|5\n"
    )

    expected = [
        {"name": "Notebook", "category": "Office Supplies", "quantity": 10},
        {"name": "Laptop", "category": "Electronics", "quantity": 5}
    ]

    # Act
    result = load_inventory(inventory_file)

    # Assert
    assert result == expected



def test_load_inventory_integer_quantity(tmp_path):
    # Arrange
    inventory_file = tmp_path / "inventory.txt"
    inventory_file.write_text("Notebook|Office Supplies|10\n")

    # Act
    result = load_inventory(inventory_file)

    # Assert
    assert result[0]["quantity"] == 10



def test_load_inventory_blank_lines(tmp_path):
    # Arrange
    inventory_file = tmp_path / "inventory.txt"
    inventory_file.write_text(
        "Notebook|Office Supplies|10\n"
        "\n"
        "\n"
        "\n"
        "Laptop|Electronics|5\n"
    )

    # Act
    result = load_inventory(inventory_file)

    # Assert
    assert len(result) == 2
    assert result[0]["name"] == "Notebook"
    assert result[1]["name"] == "Laptop"



def test_load_inventory_missing_file(tmp_path):
    # Arrange
    inventory_file = tmp_path / "missing.txt"
    expected = []

    # Act
    result = load_inventory(inventory_file)

    # Assert
    assert result == expected



def test_save_inventory_multiple_items(tmp_path):
    # Arrange
    inventory_file = tmp_path / "inventory.txt"

    inventory = [
        {"name": "Notebook", "category": "Office Supplies", "quantity": 10},
        {"name": "Laptop", "category": "Electronics", "quantity": 5}
    ]

    expected = (
        "Notebook|Office Supplies|10\n"
        "Laptop|Electronics|5\n"
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



def test_save_load_round_trip(tmp_path):
    # Arrange
    inventory_file = tmp_path / "inventory.txt"

    inventory = [
        {"name": "Notebook", "category": "Office Supplies", "quantity": 10},
        {"name": "Laptop", "category": "Electronics", "quantity": 5}
    ]

    # Act
    save_inventory(inventory, inventory_file)
    result = load_inventory(inventory_file)

    # Assert
    assert result == inventory