from products import Product  # Importing Product from the products module


class Store:
    """
    A class to represent a store that manages a collection of products.

    Attributes:
    products (list): A list of products available in the store.

    Methods:
    add_product(product): Adds a new product to the store.
    remove_product(product): Removes a product from the store.
    get_total_quantity(): Returns the total quantity of all active products in the store.
    get_all_products(): Returns a list of all active products in the store.
    order(shopping_list):
        Processes an order and returns the total price for the given list
        of products and quantities.
    """

    def __init__(self, products=None):
        """
        Initializes a new Store instance with a list of products.

        Args:
        products (list, optional): A list of Product instances.
        Defaults to an empty list if not provided.
        """
        if products is None:
            products = []
        self.products = products  # List of products in the store

    def add_product(self, product):
        """
        Adds a new product to the store.

        Args:
        product (Product): The product to add to the store.
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store.

        Args:
        product (Product): The product to remove from the store.

        Raises:
        ValueError: If the product is not found in the store.
        """
        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError(f"Product {product.name} not found in the store.")

    def get_total_quantity(self):
        """
        Returns the total quantity of all active products in the store.

        Returns:
        int: The total quantity of active products.
        """
        total = 0
        for product in self.products:
            if product.is_active():
                total += product.get_quantity()
        return total

    def get_all_products(self):
        """
        Returns a list of all active products in the store.

        Returns:
        list: A list of active Product instances.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """
        Processes an order
        Returns the total price for the given list of products and quantities.

        Args:
        shopping_list (list): A list of tuples, each containing a Product and the desired quantity.

        Returns:
        float: The total price of the order.

        Raises:
        TypeError:
            If any item in the shopping list is not a Product instance.
        ValueError:
            If a product is not available, the quantity is zero or negative,
            or there is insufficient stock.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            if not isinstance(product, Product):
                raise TypeError("Each item in the shopping list must be a Product instance.")
            if not product.is_active():
                raise ValueError(f"Product {product.name} is no longer available.")
            if quantity <= 0:
                raise ValueError("Quantity must be greater than zero.")
            try:
                total_price += product.buy(quantity)
            except ValueError as error:
                raise ValueError(f"Error while purchasing {product.name}: {error}") from error
        return total_price


def test():
    """
    Main function to demonstrate the functionality of the Store and Product classes
    by creating product instances, adding them to a store, processing an order,
    and displaying the total price of the order.
    """
    # Create a list of products using the Product class
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    # Create a Store instance with the product list
    best_buy = Store(product_list)

    # Get all active products in the store
    products = best_buy.get_all_products()

    # Print the total quantity of active products
    print(f"Total quantity of active products: {best_buy.get_total_quantity()}")

    # Create an order with specific quantities of products: Order 1 MacBook and 2 Bose earbuds
    order_total = best_buy.order([(products[0], 1), (products[1], 2)])

    print(f"Total order price: ${order_total}")


if __name__ == '__main__':
    test()
