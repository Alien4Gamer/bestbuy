class Product:
    def __init__(self, name, price, quantity):
        try:
            if not name or not isinstance(name, str):  # Ensure name is a non-empty string
                raise ValueError("Name cannot be empty and must be a string.")
            if not isinstance(price, (int, float)) or price < 0:  # Ensure price is a positive number
                raise ValueError("Price must be a positive number.")
            if not isinstance(quantity, int) or quantity < 0:  # Ensure quantity is a non-negative integer
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
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        if self.active:
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        return f"{self.name} is currently unavailable."

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        total_price = quantity * self.price
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return total_price


def main():
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
    main()
