from project import add_item, remove_item, move_item
import pytest

@pytest.fixture
def inventory():
    return {
        "dry_storage": {},
        "wine_room": {},
        "fridge": {},
        "freezer": {},
        "shelf": {}
    }

def test_add_item_new(inventory):
    add_item(inventory, "shelf", "vodka", 3)
    assert inventory["shelf"]["vodka"] == 3

def test_add_item_existing(inventory):
    add_item(inventory, "shelf", "vodka", 2)
    add_item(inventory, "shelf", "vodka", 3)
    assert inventory["shelf"]["vodka"] == 5

def test_add_item_invalid_location(inventory):
    with pytest.raises(ValueError):
        add_item(inventory, "garage", "vodka", 3)

def test_add_item_negative_quantity(inventory):
    with pytest.raises(ValueError):
        add_item(inventory, "shelf", "vodka", -5)

def test_add_item_zero_quantity(inventory):
    with pytest.raises(ValueError):
        add_item(inventory, "shelf", "vodka", 0)

