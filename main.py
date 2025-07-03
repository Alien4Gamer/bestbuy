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


def display_products(store):
    """
    Lists all available products in the store.

    Args:
        store (Store): An instance of the Store class with available products.
    """
    print("\nAvailable products:")
    for product in store.get_all_products():
        print(product.show())


def display_total_quantity(store):
    """
    Displays the total quantity of products in the store.

    Args:
        store (Store): An instance of the Store class with available products.
    """
    print(f"\nTotal quantity of products in store: {store.get_total_quantity()}")


def handle_order(store):
    """
    Allows the user to place an order by selecting products and specifying quantities.
    It checks product stock availability and updates the store's inventory only after confirmation.
    """
    shopping_list = []

    print("\nWhen you want to finish the order, enter empty text.")

    while True:
        display_products(store)

        product_choice = input("\nWhich product # do you want? ").strip()
        if product_choice == "":
            break

        try:
            product_choice = int(product_choice) - 1
            all_products = store.get_all_products()

            if product_choice < 0 or product_choice >= len(all_products):
                print("Error: Invalid product selection!")
                continue

            product = all_products[product_choice]

            quantity = int(input("What amount do you want? ").strip())
            if quantity <= 0:
                print("Error: Quantity must be greater than zero.")
                continue

            # Check if enough stock is available
            if product.get_quantity() < quantity:
                print("Error while making order! Quantity larger than what exists.")
                continue

            # Add to shopping list WITHOUT updating stock yet
            shopping_list.append((product, quantity))
            print("Product added to list!")

        except ValueError:
            print("Error: Invalid input. Please enter valid product number and quantity.")

    if shopping_list:
        try:
            total_price = store.order(shopping_list)  # This should handle quantity deduction internally
            print(f"\nOrder successfully placed! Total price: ${total_price:.2f}")
        except ValueError as error:
            print(f"Error while placing order: {error}")
    else:
        print("No products selected for the order.")


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
            display_products(store)
        elif choice == "2":
            display_total_quantity(store)
        elif choice == "3":
            handle_order(store)
        elif choice == "4":
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice, please choose a valid option.")

def main():
    """
    This program simulates a Best Buy store where users can view, order products, and check inventory.

    Initializes the store with a default set of products and starts the menu-driven interface.
    This function acts as the entry point of the program, preparing a store instance
    and launching user interaction through a command-line interface.
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
