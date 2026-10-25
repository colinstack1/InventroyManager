"""Automates unit tests for the Inventory Manager application."""

import pytest

from inventory_manager import (
    load_inventory,
    save_inventory,
    find_matching_items,
    remove_item_by_number,
    update_item_quantity,
    validate_new_item,
    calculate_summary,
)

@pytest.fixture
def sample_inventory():
    """Provide reusable inventory data for multiple tests."""
    return [
        {"name": "Laptop", "category": "Computers", "quantity": 10},
        {"name": "Mouse", "category": "Accessories", "quantity": 3},
        {"name": "Keyboard", "category": "Accessories", "quantity": 5},
        {"name": "Monitor", "category": "Displays", "quantity": 8},
    ]

def test_load_inventory_valid_file(tmp_path):
    # Arrange
    test_file = tmp_path / "inventory.txt"
    test_file.write_text(
        "Laptop|Computers|10\n"
        "Mouse|Accessories|3\n"
    )

    expected = [
        {"name": "Laptop", "category": "Computers", "quantity": 10},
        {"name": "Mouse", "category": "Accessories", "quantity": 3},
    ]

    # Act
    result = load_inventory(test_file)

    # Assert
    assert result == expected


def test_load_inventory_ignores_blank_lines(tmp_path):
    # Arrange
    test_file = tmp_path / "inventory.txt"
    test_file.write_text(
        "Laptop|Computers|10\n"
        "\n"
        "Mouse|Accessories|3\n"
    )

    # Act
    result = load_inventory(test_file)

    # Assert
    assert len(result) == 2
    assert result[0]["name"] == "Laptop"
    assert result[1]["name"] == "Mouse"


def test_load_inventory_missing_file(tmp_path):
    # Arrange
    test_file = tmp_path / "missing_inventory.txt"

    # Act
    result = load_inventory(test_file)

    # Assert
    assert result == []



def test_save_inventory_writes_correct_format(tmp_path):
    # Arrange
    test_file = tmp_path / "inventory.txt"

    inventory = [
        {"name": "Laptop", "category": "Computers", "quantity": 10},
        {"name": "Mouse", "category": "Accessories", "quantity": 3},
    ]

    expected = "Laptop|Computers|10\nMouse|Accessories|3\n"

    # Act
    save_inventory(inventory, test_file)

    # Assert
    assert test_file.read_text() == expected


def test_save_empty_inventory(tmp_path):
    # Arrange
    test_file = tmp_path / "inventory.txt"
    inventory = []

    # Act
    save_inventory(inventory, test_file)

    # Assert
    assert test_file.exists()
    assert test_file.read_text() == ""


def test_save_and_load_inventory_round_trip(tmp_path, sample_inventory):
    # Arrange
    test_file = tmp_path / "inventory.txt"

    # Act
    save_inventory(sample_inventory, test_file)
    result = load_inventory(test_file)

    # Assert
    assert result == sample_inventory


def test_search_exact_match(sample_inventory):
    # Arrange
    search_term = "Laptop"

    # Act
    result = find_matching_items(sample_inventory, search_term)

    # Assert
    assert result == [sample_inventory[0]]


def test_search_partial_match(sample_inventory):
    # Arrange
    search_term = "lap"

    # Act
    result = find_matching_items(sample_inventory, search_term)

    # Assert
    assert result == [sample_inventory[0]]


def test_search_case_insensitive(sample_inventory):
    # Arrange
    search_term = "LAPTOP"

    # Act
    result = find_matching_items(sample_inventory, search_term)

    # Assert
    assert result == [sample_inventory[0]]


def test_search_multiple_matches(sample_inventory):
    # Arrange
    search_term = "o"

    # Act
    result = find_matching_items(sample_inventory, search_term)

    # Assert
    assert result == [
        sample_inventory[0],  # Laptop
        sample_inventory[1],  # Mouse
        sample_inventory[2],  # Keyboard
        sample_inventory[3],  # Monitor
    ]


def test_search_no_matches(sample_inventory):
    # Arrange
    search_term = "Printer"

    # Act
    result = find_matching_items(sample_inventory, search_term)

    # Assert
    assert result == []


def test_search_empty_or_whitespace(sample_inventory):
    # Arrange
    search_term = "   "

    # Act
    result = find_matching_items(sample_inventory, search_term)

    # Assert
    assert result == []



def test_remove_first_item(sample_inventory):
    # Arrange
    expected_remaining = sample_inventory[1:].copy()

    # Act
    removed_item = remove_item_by_number(sample_inventory, 1)

    # Assert
    assert removed_item["name"] == "Laptop"
    assert sample_inventory == expected_remaining


def test_remove_middle_item(sample_inventory):
    # Arrange
    expected_names = ["Laptop", "Keyboard", "Monitor"]

    # Act
    removed_item = remove_item_by_number(sample_inventory, 2)

    # Assert
    assert removed_item["name"] == "Mouse"
    assert [item["name"] for item in sample_inventory] == expected_names


def test_remove_last_item(sample_inventory):
    # Arrange
    expected_names = ["Laptop", "Mouse", "Keyboard"]

    # Act
    removed_item = remove_item_by_number(sample_inventory, 4)

    # Assert
    assert removed_item["name"] == "Monitor"
    assert [item["name"] for item in sample_inventory] == expected_names


@pytest.mark.parametrize(
    "item_number",
    [0, -1, 5],
    ids=["zero", "negative-number", "out-of-range"],
)
def test_remove_invalid_item_number(sample_inventory, item_number):
    # Arrange
    original_inventory = [item.copy() for item in sample_inventory]

    # Act
    result = remove_item_by_number(sample_inventory, item_number)

    # Assert
    assert result is None
    assert sample_inventory == original_inventory


def test_update_valid_quantity(sample_inventory):
    # Arrange
    item_number = 1
    new_quantity = 25

    # Act
    result = update_item_quantity(sample_inventory, item_number, new_quantity)

    # Assert
    assert result is True
    assert sample_inventory[0]["quantity"] == 25


def test_update_quantity_to_zero(sample_inventory):
    # Arrange
    item_number = 2
    new_quantity = 0

    # Act
    result = update_item_quantity(sample_inventory, item_number, new_quantity)

    # Assert
    assert result is True
    assert sample_inventory[1]["quantity"] == 0


def test_update_only_selected_item(sample_inventory):
    # Arrange
    original_inventory = [item.copy() for item in sample_inventory]

    # Act
    result = update_item_quantity(sample_inventory, 2, 20)

    # Assert
    assert result is True
    assert sample_inventory[1]["quantity"] == 20
    assert sample_inventory[0] == original_inventory[0]
    assert sample_inventory[2:] == original_inventory[2:]


@pytest.mark.parametrize(
    "item_number",
    [0, -1, 5],
    ids=["zero", "negative-number", "out-of-range"],
)
def test_update_invalid_item_number(sample_inventory, item_number):
    # Arrange
    original_inventory = [item.copy() for item in sample_inventory]

    # Act
    result = update_item_quantity(sample_inventory, item_number, 10)

    # Assert
    assert result is False
    assert sample_inventory == original_inventory


def test_update_rejects_negative_quantity(sample_inventory):
    # Arrange
    original_inventory = [item.copy() for item in sample_inventory]

    # Act
    result = update_item_quantity(sample_inventory, 1, -5)

    # Assert
    assert result is False
    assert sample_inventory == original_inventory



def test_validate_new_item_accepts_valid_item(sample_inventory):
    # Arrange
    name = "Webcam"
    category = "Electronics"
    quantity = 10

    # Act
    result = validate_new_item(
        sample_inventory, name, category, quantity
    )

    # Assert
    assert result is None


@pytest.mark.parametrize(
    "name, category, quantity, expected_error",
    [
        ("", "Electronics", 5, "Item name cannot be empty."),
        ("Webcam", "", 5, "Category cannot be empty."),
        ("Web|cam", "Electronics", 5,
         "Item name cannot contain the | character."),
        ("Webcam", "Elect|ronics", 5,
         "Category cannot contain the | character."),
        ("Webcam", "Electronics", -3,
         "Quantity must be a nonnegative whole number."),
        ("Laptop", "Electronics", 5,
         "An item with that name already exists."),
        ("lApToP", "Electronics", 5,
         "An item with that name already exists."),
    ],
    ids=[
        "empty-name",
        "empty-category",
        "pipe-in-name",
        "pipe-in-category",
        "negative-quantity",
        "duplicate-name",
        "duplicate-different-case",
    ],
)
def test_validate_new_item_rejects_invalid_data(
    sample_inventory, name, category, quantity, expected_error
):
    # Arrange
    original_inventory = [
        item.copy() for item in sample_inventory
    ]

    # Act
    result = validate_new_item(
        sample_inventory, name, category, quantity
    )

    # Assert
    assert result == expected_error
    assert sample_inventory == original_inventory


def test_validate_new_item_rejects_nonnumeric_quantity(
    sample_inventory
):
    # Arrange
    name = "Webcam"
    category = "Electronics"
    quantity = "five"

    # Act
    result = validate_new_item(
        sample_inventory, name, category, quantity
    )

    # Assert
    assert result == "Quantity must be a nonnegative whole number."


def test_validate_new_item_accepts_zero_quantity(sample_inventory):
    # Arrange
    name = "Webcam"
    category = "Electronics"
    quantity = 0

    # Act
    result = validate_new_item(
        sample_inventory, name, category, quantity
    )

    # Assert
    assert result is None



# ---------------------------------------------------------
# Inventory Summary Tests
# ---------------------------------------------------------

def test_summary_unique_items(sample_inventory):
    # Arrange
    expected = 4

    # Act
    result = calculate_summary(sample_inventory)

    # Assert
    assert result["unique_items"] == expected


def test_summary_total_quantity(sample_inventory):
    # Arrange
    expected = 26

    # Act
    result = calculate_summary(sample_inventory)

    # Assert
    assert result["total_quantity"] == expected


def test_summary_low_stock_items(sample_inventory):
    # Arrange
    expected = 1

    # Act
    result = calculate_summary(sample_inventory)

    # Assert
    assert result["low_stock_items"] == expected


def test_summary_category_counts(sample_inventory):
    # Arrange
    expected = {
        "computers": 1,
        "accessories": 2,
        "displays": 1,
    }

    # Act
    result = calculate_summary(sample_inventory)

    actual = {
        category: info["count"]
        for category, info in result["category_counts"].items()
    }

    # Assert
    assert actual == expected


def test_summary_categories_ignore_capitalization():
    # Arrange
    inventory = [
        {"name": "Mouse", "category": "Accessories", "quantity": 3},
        {"name": "Keyboard", "category": "ACCESSORIES", "quantity": 5},
        {"name": "Cable", "category": "accessories", "quantity": 8},
    ]

    # Act
    result = calculate_summary(inventory)

    # Assert
    assert result["category_counts"]["accessories"]["count"] == 3
    assert len(result["category_counts"]) == 1


def test_summary_empty_inventory():
    # Arrange
    inventory = []

    # Act
    result = calculate_summary(inventory)

    # Assert
    assert result == {
        "unique_items": 0,
        "total_quantity": 0,
        "low_stock_items": 0,
        "category_counts": {},
    }


@pytest.mark.parametrize(
    "quantity, expected_low_stock",
    [
        (4, 1),
        (5, 0),
    ],
    ids=["quantity-four-low-stock", "quantity-five-not-low-stock"],
)
def test_summary_low_stock_boundary(quantity, expected_low_stock):
    # Arrange
    inventory = [
        {
            "name": "Test Item",
            "category": "Electronics",
            "quantity": quantity,
        }
    ]

    # Act
    result = calculate_summary(inventory)

    # Assert
    assert result["low_stock_items"] == expected_low_stock
