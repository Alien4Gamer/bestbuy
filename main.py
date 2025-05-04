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
    Allows the user to place an order by selecting products and specifying quantities.
    It checks product stock availability and updates the store's inventory accordingly.
    After the user completes their selection, the total price of the order is calculated and displayed.

    Args:
        store (Store): An instance of the Store class that holds the available products and inventory details.
    """
    shopping_list = []
    stock_dict = {}

    # Initialize the stock dictionary with both quantity and price
    all_products = store.get_all_products()
    for product in all_products:
        stock_dict[product.name] = {
            "quantity": product.get_quantity(),
            "price": product.get_price()
        }

    print("\nWhen you want to finish the order, enter empty text.")

    while True:
        print("\nSelect a product and quantity:")

        # Display products with their index, price, and quantity from the dictionary
        for i, product in enumerate(all_products, 1):
            product_id = product.name
            quantity = stock_dict[product_id]["quantity"]
            price = stock_dict[product_id]["price"]
            print(f"{i}. {product.name}, Price: {price}, Quantity: {quantity}")

        product_choice = input("\nWhich product # do you want? ").strip()
        if product_choice == "":
            break

        try:
            product_choice = int(product_choice) - 1  # Convert to zero-based index
            if product_choice < 0 or product_choice >= len(all_products):
                print("Error: Invalid product selection!")
                continue
            product = all_products[product_choice]
            product_id = product.name

            quantity = int(input("What amount do you want? ").strip())
            if quantity <= 0:
                print("Error: Quantity must be greater than zero.")
                continue

            # Check if enough stock is available using the stock_dict
            if stock_dict[product_id]["quantity"] < quantity:
                print("Error while making order! Quantity larger than what exists.")
                continue

            # Add to shopping list and update the stock dictionary
            shopping_list.append((product, quantity))
            stock_dict[product_id]["quantity"] -= quantity  # Update stock

            print("Product added to list!")

        except ValueError:
            print("Error: Invalid input. Please enter valid product number and quantity.")

    if shopping_list:
        # Process the order
        try:
            total_price = store.order(shopping_list)
            print(f"\nOrder successfully placed! Total price: ${total_price:.2f}")
        except ValueError as error:
            print(f"Error: {error}")
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
