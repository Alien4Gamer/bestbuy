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

    def __init__(self, products):
        """
        Initializes a new Store instance with a list of products.

        Args:
        products (list): A list of Product instances.

        Raises:
        ValueError: If products is not a list, is empty, or contains non-Product instances.
        """
        if not isinstance(products, list) or not products:
            raise ValueError("Products must be a non-empty list of Product instances.")
        if not all(isinstance(p, Product) for p in products):
            raise ValueError("All items in the products list must be instances of Product.")

        self.products = products

    def add_product(self, product):
        """
        Adds a new product to the store.

        Args:
        product (Product): The product to add to the store.
        """
        if any(p.name == product.name for p in self.products):
            raise ValueError(f"Product '{product.name}' already exists in the store.")
        self.products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store.

        Args:
        product (Product): The product to remove from the store.

        Raises:
        ValueError: If the product is not found in the store.
        """
        for p in self.products:
            if p.name == product.name:
                self.products.remove(p)
                return
        raise ValueError(f"Product '{product.name}' not found in the store.")

    def get_total_quantity(self):
        """
        Returns the total quantity of all active products in the store.

        Returns:
        int: The total quantity of active products.
        """
        return sum(product.get_quantity() for product in self.products if product.is_active())

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
            if product.get_quantity() < quantity:
                raise ValueError(
                    f"Not enough stock available for {product.name}. "
                    f"Available: {product.get_quantity()}, Requested: {quantity}")
            try:
                total_price += product.buy(quantity)
            except ValueError as error:
                raise ValueError(f"Error while purchasing {product.name}: {error}") from error
        return total_price
