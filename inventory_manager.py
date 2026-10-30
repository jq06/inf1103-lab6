import json
import os

# Store inventory as a list of dictionaries
inventory = []


def display_all():
    print("\nCurrent Inventory")
    if not inventory:
        print("No products available.")
        return

    for prod in inventory:
        print(
            f"ID: {prod['id']} | Name: {prod['name']} | "
            f"Price: ${prod['price']:.2f} | Stock: {prod['stock']}"
        )


def add_product():
    print("\nAdd New Product")
    prod_id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()

    try:
        price = float(input("Price: ").strip())
        stock = int(input("Stock Quantity: ").strip())
    except ValueError:
        print("Invalid input for price or stock. Product not added.")
        return

    inventory.append(
        {"id": prod_id, "name": name, "price": price, "stock": stock}
    )
    print("Product added successfully!")


def update_stock():
    print("\nUpdate Stock")
    prod_id = input("Enter Product ID: ").strip()

    for prod in inventory:
        if prod["id"].lower() == prod_id.lower():
            print(
                f"\nProduct Found:\nName: {prod['name']}\nCurrent Stock: {prod['stock']}\n"
            )
            try:
                new_stock = int(input("New Stock Quantity: ").strip())
                prod["stock"] = new_stock
                print("Stock updated successfully!")
            except ValueError:
                print("Invalid stock number.")
            return

    print("Product not found.")


def search_product():
    print("\nSearch Product")
    prod_id = input("Enter Product ID: ").strip()

    for prod in inventory:
        if prod["id"].lower() == prod_id.lower():
            print("Product Found")
            print("-" * 35)
            print(f"ID: {prod['id']}")
            print(f"Name: {prod['name']}")
            print(f"Price: ${prod['price']:.2f}")
            print(f"Stock: {prod['stock']}")
            print("-" * 35)
            return

    print("\nProduct not found.")

def load_inventory():
    global inventory

    if os.path.exists("inventory.json"):
        print("inventory.json found.")
        try:
            with open("inventory.json", "r") as f:
                inventory = json.load(f)
            print("Inventory loaded successfully.")
        except json.JSONDecodeError:
            print("Error loading inventory.json, starting with empty inventory.")
            inventory = []
    else:
        print("inventory.json not found. Starting with empty inventory.")
        inventory = []

def save_inventory():
    print("\nSaving inventory...")
    with open("inventory.json", "w") as f:
        json.dump(inventory, f, indent=4)
    print("Inventory saved successfully to inventory.json.")


def main():
    print("INVENTORY MANAGEMENT SYSTEM")
    load_inventory()

    while True:
        print("\nMENU")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")

        choice = input("Enter option: ").strip()

        if choice == "1":
            display_all()
        elif choice == "2":
            add_product()
        elif choice == "3":
            update_stock()
        elif choice == "4":
            search_product()
        elif choice == "5":
            save_inventory()
        elif choice == "6":
            print("\nSaving inventory before exit...")
            save_inventory()
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()