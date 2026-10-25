"""Automates unit tests for the Inventory Manager application."""

import pytest

from inventory_manager import (
    load_inventory,
    save_inventory,
    find_matching_items,
)

@pytest.fixture
def sample_inventory():
    """Provide reusable inventory data for multiple tests."""
    return [
        {"name": "Laptop", "category": "Computers", "quantity": 10},
        {"name": "Mouse", "category": "Accessories", "quantity": 10},
        {"name": "Keyboard", "category": "Accessories", "quantity": 10},
        {"name": "Monitor", "category": "Displays", "quantity": 10},

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