from file_handler import load_inventory, save_inventory
from product import Product


def main():
    print("INVENTORY MANAGEMENT SYSTEM")
    inventory = load_inventory()

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
            inventory.display_all()

        elif choice == "2":
            print("\nAdd New Product")
            prod_id = input("Product ID: ").strip()
            name = input("Product Name: ").strip()
            try:
                price = float(input("Price: ").strip())
                stock = int(input("Stock Quantity: ").strip())
            except ValueError:
                print("Invalid input for price or stock. Product not added.")
                continue
            inventory.add_product(Product(prod_id, name, price, stock))
            print("Product added successfully!")

        elif choice == "3":
            print("\nUpdate Stock")
            prod_id = input("Enter Product ID: ").strip()
            product = inventory.search_product(prod_id)
            if product is None:
                print("Product not found.")
                continue
            print(f"\nProduct Found:\nName: {product.name}\nCurrent Stock: {product.stock}\n")
            try:
                new_stock = int(input("New Stock Quantity: ").strip())
                product.update_stock(new_stock)
                print("Stock updated successfully!")
            except ValueError:
                print("Invalid stock number.")

        elif choice == "4":
            print("\nSearch Product")
            prod_id = input("Enter Product ID: ").strip()
            product = inventory.search_product(prod_id)
            if product is None:
                print("\nProduct not found.")
            else:
                print("Product Found")
                product.display_information()

        elif choice == "5":
            save_inventory(inventory)

        elif choice == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()