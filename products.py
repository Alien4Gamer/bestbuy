class Product:
    """
    A class to represent a product with a name, price, quantity, and status.

    Attributes:
    name (str): The name of the product.
    price (float): The price of the product.
    quantity (int): The quantity of the product in stock.
    active (bool): The status of the product, indicating whether it is available for purchase.

    Methods:
    get_quantity(): Returns the current quantity of the product.
    set_quantity(quantity):
        Sets the quantity of the product and deactivates it if the quantity reaches zero.
    is_active(): Returns whether the product is currently active.
    activate(): Activates the product, setting its status to active.
    deactivate(): Deactivates the product, setting its status to inactive.
    show():
        Returns a string representing the product's details if active,
        or indicates that it is unavailable.
    buy(quantity):
        Simulates buying the product,
        reducing the stock and returning the total price of the purchase.
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a new Product instance with a name, price, and quantity.

        Args:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product in stock.

        Raises:
        ValueError:
            If any input is invalid
            (name is empty or not a string, price is negative, or quantity is negative).
        """
        try:
            if not name or not isinstance(name, str):
                raise ValueError("Name cannot be empty and must be a string.")
            if not isinstance(price, (int, float)) or price < 0:
                raise ValueError("Price must be a positive number.")
            if not isinstance(quantity, int) or quantity < 0:
                raise ValueError("Quantity must be a non-negative integer.")

            self.name = name
            self.price = price
            self.quantity = quantity
            self.active = True  # Product is active by default

        except ValueError as error:
            print(f"Error: {error}")
            self.name = None  # Assign None or some default value if initialization fails
            self.price = None
            self.quantity = None
            self.active = False

    def get_quantity(self):
        """
        Returns the current quantity of the product.

        Returns:
        int: The current quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Sets the quantity of the product and deactivates it if the quantity reaches zero.

        Args:
        quantity (int): The new quantity of the product.

        Raises:
        ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """
        Returns whether the product is currently active.

        Returns:
        bool: True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Activates the product, setting its status to active.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product, setting its status to inactive.
        """
        self.active = False

    def show(self):
        """
        Returns a string representing the product's details if active,
        or indicates that it is unavailable.

        Returns:
        str: A string representing the product's details or its unavailability.
        """
        if self.active:
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        return f"{self.name} is currently unavailable."

    def buy(self, quantity):
        """
        Simulates buying the product,
        reducing the stock and returning the total price of the purchase.

        Args:
        quantity (int): The number of units of the product to purchase.

        Returns:
        float: The total price for the purchased quantity.

        Raises:
        ValueError:
            If the quantity to buy is less than or equal to zero or exceeds the available stock.
        """
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        total_price = quantity * self.price
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return total_price


def test():
    """
    Main function to demonstrate the functionality of the Product class
    by creating product instances, buying products, and displaying product details.
    """
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == '__main__':
    test()
