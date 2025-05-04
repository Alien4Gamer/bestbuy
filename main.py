from products import Product
from store import Store

def show_menu():
    """
    Displays the store menu options to the user.
    """
    print("\nStore Menu:")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def handle_product_list(store):
    """
    Lists all available products in the store.

    Args:
        store (Store): An instance of the Store class with available products.
    """
    print("\nAvailable products:")
    for product in store.get_all_products():
        print(product.show())


def handle_total_quantity(store):
    """
    Displays the total quantity of products in the store.

    Args:
        store (Store): An instance of the Store class with available products.
    """
    print(f"\nTotal quantity of products in store: {store.get_total_quantity()}")


def handle_order(store):
    """
    Allows the user to make an order by entering product names and quantities.

    Args:
        store (Store): An instance of the Store class with available products.
    """
    shopping_list = []
    print("\nEnter products and quantities to order (e.g., 'MacBook Air M2, 1')."
            "Type 'done' when finished.")
    while True:
        order_input = input("Enter product name and quantity (or 'done' to finish): ")
        if order_input.lower() == 'done':
            break
        try:
            name, quantity = order_input.split(',')
            quantity = int(quantity.strip())
            # Find the product by name
            product = next((product for product in store.get_all_products()
                            if product.name.lower() == name.strip().lower()), None)
            if product:
                shopping_list.append((product, quantity))
            else:
                print(f"Product {name.strip()} not found.")
        except ValueError:
            print("Invalid input. Please enter in the format 'Product Name, Quantity'.")

    # Process the order
    try:
        total_price = store.order(shopping_list)
        print(f"\nOrder successfully placed! Total price: ${total_price:.2f}")
    except ValueError as error:
        print(f"Error: {error}")


def start(store):
    """
    Starts the store menu interaction where users can list products,
    view total quantity in the store, place an order, or quit the program.

    Args:
        store (Store): An instance of the Store class with available products.
    """
    while True:
        show_menu()

        # Get the user's choice
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            handle_product_list(store)
        elif choice == "2":
            handle_total_quantity(store)
        elif choice == "3":
            handle_order(store)
        elif choice == "4":
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice, please choose a valid option.")

def main():
    """
    Initiates and starts the store interaction process.
    """
    # Setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = Store(product_list)

    start(best_buy)

if __name__ == '__main__':
    main()
