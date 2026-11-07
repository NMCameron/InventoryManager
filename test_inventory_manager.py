import pytest
from inventory_manager import load_inventory, save_inventory



@pytest.fixture
def sample_inventory():
    return [
        {"name": "Notebook", "category": "Office", "quantity": 4},
        {"name": "Laptop", "category": "Electronics", "quantity": 10},
        {"name": "Pen", "category": "office", "quantity": 5},
        {"name": "Mouse", "category": "Electronics", "quantity": 0},
    ]



def test_load_valid_file(tmp_path):
    # Arrange
    file = tmp_path / "inventory.txt"
    file.write_text("Notebook|Office|10\n")

    # Act
    inventory = load_inventory(file)

    # Assert
    assert inventory == [{"name": "Notebook", "category": "Office", "quantity": 10}]



def test_load_quantity_integer(tmp_path):
    # Arrange
    file = tmp_path / "inventory.txt"
    file.write_text("Notebook|Office|10\n")

    # Act
    inventory = load_inventory(file)

    # Assert
    assert inventory[0]["quantity"] == 10



def test_load_ignores_blanks(tmp_path):
    # Arrange
    file = tmp_path / "inventory.txt"
    file.write_text("Notebook|Office|10\n\n\nLaptop|Electronics|5\n\n")

    # Act
    inventory = load_inventory(file)

    # Assert
    assert len(inventory) == 2
    assert inventory[1]["name"] == "Laptop"



def test_load_missing_file(tmp_path):
    # Arrange
    file = tmp_path / "not_inventory.txt"

    # Act
    inventory = load_inventory(file)

    # Assert
    assert inventory == []



def test_load_empty_file(tmp_path):
    # Arrange
    file = tmp_path / "inventory.txt"
    file.write_text("")

    # Act
    inventory = load_inventory(file)

    # Assert
    assert inventory == []


@pytest.mark.parametrize(
    "quantity",
    ["0", "4", "5"],
    ids=["zero", "low_stock_boundary", "not_low_stock_boundary"],
)
def test_load_different_quantities(tmp_path, quantity):
    # Arrange
    file = tmp_path / "inventory.txt"
    file.write_text(f"Notebook|Office|{quantity}\n")

    # Act
    inventory = load_inventory(file)

    # Assert
    assert inventory[0]["quantity"] == int(quantity)



def test_save_multiple_items(tmp_path, sample_inventory):
    # Arrange
    file = tmp_path / "inventory.txt"

    # Act
    save_inventory(sample_inventory, file)

    # Assert
    assert file.read_text() == (
        "Notebook|Office|4\n"
        "Laptop|Electronics|10\n"
        "Pen|office|5\n"
        "Mouse|Electronics|0\n"
    )



def test_save_empty_inventory(tmp_path):
    # Arrange
    file = tmp_path / "inventory.txt"
    inventory = []

    # Act
    save_inventory(inventory, file)

    # Assert
    assert file.read_text() == ""



def test_save_and_load_round_trip(tmp_path, sample_inventory):
    # Arrange
    file = tmp_path / "inventory.txt"

    # Act
    save_inventory(sample_inventory, file)
    inventory = load_inventory(file)

    # Assert
    assert inventory == sample_inventory



def test_save_overwrites_existing_file(tmp_path, sample_inventory):
    # Arrange
    file = tmp_path / "inventory.txt"
    file.write_text("Old|Category|99\n")

    # Act
    save_inventory(sample_inventory, file)

    # Assert
    assert "Old|Category|99" not in file.read_text()
    assert len(load_inventory(file)) == 4



def test_save_empty_overwrites_existing_file(tmp_path, sample_inventory):
    # Arrange
    file = tmp_path / "inventory.txt"
    save_inventory(sample_inventory, file)

    # Act
    save_inventory([], file)

    # Assert
    assert file.read_text() == ""



def test_save_preserves_item_order(tmp_path, sample_inventory):
    # Arrange
    file = tmp_path / "inventory.txt"

    # Act
    save_inventory(sample_inventory, file)
    inventory = load_inventory(file)

    # Assert
    assert [item["name"] for item in inventory] == ["Notebook", "Laptop", "Pen", "Mouse"]



def test_save_preserves_category_capitalization(tmp_path, sample_inventory):
    # Arrange
    file = tmp_path / "inventory.txt"

    # Act
    save_inventory(sample_inventory, file)
    inventory = load_inventory(file)

    # Assert
    assert inventory[0]["category"] == "Office"
    assert inventory[2]["category"] == "office"



@pytest.mark.parametrize(
    "name",
    ["Notebook", "Laptop", "Pen"],
    ids=["notebook", "laptop", "pen"],
)
def test_save_different_item_names(tmp_path, name):
    # Arrange
    file = tmp_path / "inventory.txt"
    inventory = [{"name": name, "category": "Office", "quantity": 1}]

    # Act
    save_inventory(inventory, file)

    # Assert
    assert file.read_text() == f"{name}|Office|1\n"



def test_load_preserves_spaces_in_names_and_categories(tmp_path):
    # Arrange
    file = tmp_path / "inventory.txt"
    file.write_text("Red Notebook|Office Supplies|9\n")

    # Act
    inventory = load_inventory(file)

    # Assert
    assert inventory[0]["name"] == "Red Notebook"
    assert inventory[0]["category"] == "Office Supplies"



def test_save_and_load_after_adding_to_inventory(tmp_path, sample_inventory):
    # Arrange
    file = tmp_path / "inventory.txt"
    new_item = {"name": "Stapler", "category": "Office", "quantity": 2}
    sample_inventory.append(new_item)

    # Act
    save_inventory(sample_inventory, file)
    inventory = load_inventory(file)

    # Assert
    assert len(inventory) == 5
    assert inventory[-1] == new_item