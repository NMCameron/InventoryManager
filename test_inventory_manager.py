import pytest

from inventory_manager import (
    calculate_summary,
    find_matches,
    load_inventory,
    remove_item_at,
    save_inventory,
    update_item_quantity,
    validate_new_item,
)


@pytest.fixture
def sample_inventory():
    return [
        {"name": "Laptop", "category": "Electronics", "quantity": 10},
        {"name": "Laptop Charger", "category": "Electronics", "quantity": 4},
        {"name": "Phone", "category": "Electronics", "quantity": 15},
        {"name": "Phone Charger", "category": "Electronics", "quantity": 5},
        {"name": "Stapler", "category": "Office Supplies", "quantity": 8},
        {"name": "Printer Paper", "category": "Office Supplies", "quantity": 2},
    ]



def test_load_valid_inventory(tmp_path):
    # Arrange
    file_path = tmp_path / "inventory.txt"
    file_path.write_text("Laptop|Electronics|10\nStapler|Office Supplies|8\n")

    # Act
    result = load_inventory(str(file_path))

    # Assert
    assert result == [
        {"name": "Laptop", "category": "Electronics", "quantity": 10},
        {"name": "Stapler", "category": "Office Supplies", "quantity": 8},
    ]



def test_load_quantity_integer(tmp_path):
    # Arrange
    file_path = tmp_path / "inventory.txt"
    file_path.write_text("Phone|Electronics|15\n")

    # Act
    result = load_inventory(str(file_path))

    # Assert
    assert isinstance(result[0]["quantity"], int)
    assert result[0]["quantity"] == 15



def test_load_missing_file(tmp_path):
    # Arrange
    missing_path = tmp_path / "does_not_exist.txt"

    # Act
    result = load_inventory(str(missing_path))

    # Assert
    assert result == []



def test_save_writes_summary(tmp_path, sample_inventory):
    # Arrange
    file_path = tmp_path / "inventory.txt"

    # Act
    save_inventory(sample_inventory, str(file_path))

    # Assert
    lines = file_path.read_text().splitlines()
    assert lines == [
        "Laptop|Electronics|10",
        "Laptop Charger|Electronics|4",
        "Phone|Electronics|15",
        "Phone Charger|Electronics|5",
        "Stapler|Office Supplies|8",
        "Printer Paper|Office Supplies|2",
    ]



def test_save_empty_inventory(tmp_path):
    # Arrange
    file_path = tmp_path / "inventory.txt"

    # Act
    save_inventory([], str(file_path))

    # Assert
    assert file_path.read_text() == ""



def test_round_trip(tmp_path, sample_inventory):
    # Arrange
    file_path = tmp_path / "inventory.txt"

    # Act
    save_inventory(sample_inventory, str(file_path))
    loaded = load_inventory(str(file_path))

    # Assert
    assert loaded == sample_inventory



def test_search_exact_name(sample_inventory):
    # Arrange
    term = "Stapler"

    # Act
    result = find_matches(sample_inventory, term)

    # Assert
    assert result == [
        {"name": "Stapler", "category": "Office Supplies", "quantity": 8}
    ]



def test_search_ignore_case(sample_inventory):
    # Arrange
    term = "pRiNtEr pApEr"

    # Act
    result = find_matches(sample_inventory, term)

    # Assert
    assert len(result) == 1
    assert result[0]["name"] == "Printer Paper"



def test_search_no_matches(sample_inventory):
    # Arrange
    term = "Monitor"

    # Act
    result = find_matches(sample_inventory, term)

    # Assert
    assert result == []



def test_remove_first_item(sample_inventory):
    # Arrange
    item_number = 1

    # Act
    removed = remove_item_at(sample_inventory, item_number)

    # Assert
    names = [item["name"] for item in sample_inventory]
    assert removed is True
    assert names == [
        "Laptop Charger",
        "Phone",
        "Phone Charger",
        "Stapler",
        "Printer Paper",
    ]



def test_remove_last_item(sample_inventory):
    # Arrange
    item_number = len(sample_inventory)

    # Act
    removed = remove_item_at(sample_inventory, item_number)

    # Assert
    names = [item["name"] for item in sample_inventory]
    assert removed is True
    assert names == [
        "Laptop",
        "Laptop Charger",
        "Phone",
        "Phone Charger",
        "Stapler",
    ]



def test_remove_item_number_zero_is_rejected(sample_inventory):
    # Arrange
    item_number = 0

    # Act
    removed = remove_item_at(sample_inventory, item_number)

    # Assert
    assert removed is False
    assert len(sample_inventory) == 6



@pytest.mark.parametrize(
    "new_quantity",
    [25, 0],
    ids=["normal-quantity", "zero-quantity"],
)
def test_update_quantity(sample_inventory, new_quantity):
    # Arrange
    item_number = 1  # Laptop

    # Act
    updated = update_item_quantity(sample_inventory, item_number, new_quantity)

    # Assert
    assert updated is True
    assert sample_inventory[0]["quantity"] == new_quantity



def test_update_selected_item(sample_inventory):
    # Arrange
    item_number = 3  # Phone

    # Act
    update_item_quantity(sample_inventory, item_number, 99)

    # Assert
    assert sample_inventory == [
        {"name": "Laptop", "category": "Electronics", "quantity": 10},
        {"name": "Laptop Charger", "category": "Electronics", "quantity": 4},
        {"name": "Phone", "category": "Electronics", "quantity": 99},
        {"name": "Phone Charger", "category": "Electronics", "quantity": 5},
        {"name": "Stapler", "category": "Office Supplies", "quantity": 8},
        {"name": "Printer Paper", "category": "Office Supplies", "quantity": 2},
    ]



@pytest.mark.parametrize(
    "name, category, quantity_text, expected_error",
    [
        ("", "Electronics", "5", "Item name cannot be empty."),
        ("Tablet", "", "5", "Category cannot be empty."),
        (
            "Tab|let",
            "Electronics",
            "5",
            "Item name may not contain the | character.",
        ),
    ],
    ids=["empty-name", "empty-category", "pipe-in-name"],
)
def test_input_validation(sample_inventory, name, category, quantity_text, expected_error):
    # Arrange - Parameters

    # Act
    error = validate_new_item(sample_inventory, name, category, quantity_text)

    # Assert
    assert error == expected_error



@pytest.mark.parametrize(
    "quantity, expected_low_stock_count",
    [(4, 1), (5, 0)],
    ids=["quantity-4-is-low-stock", "quantity-5-is-not-low-stock"],
)
def test_low_stock(quantity, expected_low_stock_count):
    # Arrange
    inventory = [{"name": "Monitor", "category": "Electronics", "quantity": quantity}]

    # Act
    summary = calculate_summary(inventory)

    # Assert
    assert summary["low_stock_items"] == expected_low_stock_count



def test_summary_empty_inventory():
    # Arrange
    inventory = []

    # Act
    summary = calculate_summary(inventory)

    # Assert
    assert summary["unique_items"] == 0
    assert summary["total_quantity"] == 0
    assert summary["low_stock_items"] == 0
    assert summary["category_counts"] == {}