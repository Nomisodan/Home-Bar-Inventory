import json

VALID_LOCATIONS = [
    "dry_storage",
    "wine_room",
    "fridge",
    "freezer",
    "shelf",
]

def add_item(inventory, location, name, quantity):
    if location not in inventory:        
        raise ValueError(f"Invalid location: {location}")

    if quantity <= 0:
        raise ValueError("Quantity must be positive") 
    
    if name in inventory[location]:
        inventory[location][name] += quantity
    else:
        inventory[location][name] = quantity


def load_inventory(filename="inventory.json"):
    """Load inventory from JSON, creating a fresh structure if the file is missing or invalid."""
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {location: {} for location in VALID_LOCATIONS}

    # Ensure all valid locations exist even if the file was edited manually
    for location in VALID_LOCATIONS:
        if location not in data:
            data[location] = {}

    return data

def remove_item(inventory, location, name, quantity):
    if location not in inventory:        
        raise ValueError(f"Invalid location: {location}")

    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    
    if name not in inventory[location]:  
        raise ValueError(f"Item '{name}' not found in {location}")
    
    if inventory[location][name] < quantity:  
        raise ValueError(f"Insufficient stock: only {inventory[location][name]} available")
    
    inventory[location][name] -= quantity 

def move_item(inventory, name, quantity, from_location, to_location):
    remove_item(inventory, from_location, name, quantity)
    add_item(inventory, to_location, name, quantity)

def get_location_inventory(inventory, location):
    if location not in inventory:
        raise ValueError(f"Invalid location: {location}")
    
    return inventory[location].copy()

def get_global_inventory(inventory):
    global_totals = {}
    for location in inventory:
        for item, qty in inventory[location].items():
            if item in global_totals:
                global_totals[item] += qty
            else:
                global_totals[item] = qty
    return global_totals

def save_inventory(inventory, filename="inventory.json"):
    with open(filename, "w") as file:
        json.dump(inventory, file, indent=4)

def main():
    inventory = load_inventory()
    print("\nWelcome to the Home Bar Inventory System!")

    for location in VALID_LOCATIONS:
        print(f"\n{location.replace('_', ' ').title()}:")
        items = get_location_inventory(inventory, location)
        if items:
            for item, qty in items.items():
                print(f"  {item}: {qty}")
        else:
            print("  (empty)")
    
    print("\nAdding:\n- 3 vodka to dry storage\n- 2 wine to wine room\n- 6 beer to fridge\n- 1 frozen berries to freezer")

    add_item(inventory, "dry_storage", "vodka", 3)
    
    add_item(inventory, "wine_room", "wine", 2)
    
    add_item(inventory, "fridge", "beer", 6)
    
    add_item(inventory, "freezer", "frozen berries", 1)

    print("\nDry storage contains:")
    dry = get_location_inventory(inventory, "dry_storage")
    for item, qty in dry.items():
        print(f"{item}: {qty}")
    if not dry:
        print("(empty)")
    
    print("\nMoving 2 vodka from dry storage to shelf...")
    move_item(inventory, "vodka", 2, "dry_storage", "shelf")
    
    print("\nAfter moving, dry storage contains:")
    dry = get_location_inventory(inventory, "dry_storage")
    for item, qty in dry.items():
        print(f"{item}: {qty}")
    if not dry:
        print("(empty)")

    print("\nShelf now contains:")
    shelf = get_location_inventory(inventory, "shelf")
    for item, qty in shelf.items():
        print(f"{item}: {qty}")
    if not shelf:
        print("(empty)")

    print("\nGlobal inventory totals:")
    global_totals = get_global_inventory(inventory)
    for item, qty in global_totals.items():
        print(f"{item}: {qty}")
    if not global_totals:
        print("(empty)")
    
    save_inventory(inventory)
    print("\nInventory saved successfully!")

if __name__ == "__main__":
    main()