from products import Product  # Importing Product from the products module


class Store:
    def __init__(self, products=None):
        if products is None:
            products = []
        self.products = products  # List of products in the store

    def add_product(self, product):
        """Adds a new product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from the store."""
        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError(f"Product {product.name} not found in the store.")

    def get_total_quantity(self):
        """Returns the total quantity of all products in the store."""
        total = 0
        for product in self.products:
            if product.is_active():
                total += product.get_quantity()
        return total

    def get_all_products(self):
        """Returns all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """Processes an order and returns the total price for the given list of products, quantities tuples."""
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
                raise ValueError(f"Error while purchasing {product.name}: {error}")
        return total_price


def main():
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

    # Create an order with specific quantities of products
    order_total = best_buy.order([(products[0], 1), (products[1], 2)])  # Order 1 MacBook and 2 Bose earbuds

    print(f"Total order price: ${order_total}")


if __name__ == '__main__':
    main()
