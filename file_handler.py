import json
import os

from inventory import Inventory
from product import Product


def load_inventory():
    inventory = Inventory()

    if os.path.exists("inventory.json"):
        print("inventory.json found.")
        try:
            with open("inventory.json", "r") as f:
                data = json.load(f)
            for item in data:
                inventory.add_product(
                    Product(item["id"], item["name"], item["price"], item["stock"])
                )
            print("Inventory loaded successfully.")
        except json.JSONDecodeError:
            print("Error loading inventory.json, starting with empty inventory.")
            inventory = Inventory()
    else:
        print("inventory.json not found. Starting with empty inventory.")

    return inventory


def save_inventory(inventory):
    print("\nSaving inventory...")
    data = []
    for product in inventory.get_products():
        data.append(
            {
                "id": product.product_id,
                "name": product.name,
                "price": product.price,
                "stock": product.stock,
            }
        )
    with open("inventory.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Inventory saved successfully to inventory.json.")