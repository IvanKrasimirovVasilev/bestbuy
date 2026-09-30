class Product:
    """Represent a product in the store."""

    def __init__(self, name, price, quantity):
        """Create a product."""

        # Check data types
        if not isinstance(name, str):
            raise TypeError("Product name must be a string.")

        if not isinstance(price, (int, float)):
            raise TypeError("Product price must be a number.")

        if not isinstance(quantity, int):
            raise TypeError("Product quantity must be an integer.")

        # Check data values
        if not name:
            raise ValueError("Product name cannot be empty.")

        if price < 0:
            raise ValueError("Product price cannot be negative.")

        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """Return the product quantity."""
        return self.quantity

    def is_active(self):
        """Return whether the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def set_quantity(self, quantity):
        """Set the product quantity."""

        if not isinstance(quantity, (int)):
            raise TypeError("Wrong product quantity. Must be an integer.")

        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")


        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def show(self):
        """Display the product information."""
        print(self.name + ", Price: " + str(self.price) +
              ", Quantity: " + str(self.quantity))

    def buy(self, quantity):
        """Buy a quantity of the product."""

        if not isinstance(quantity, (int)):
            raise TypeError("Wrong product quantity. Must be an integer.")

        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")

        # Check if product is active
        if not self.is_active():
            raise ValueError("Product is not active.")

        if quantity > self.quantity:
            raise ValueError("Not enough " + self.name +
                             "in store. We have only " + str(self.quantity) +
                             " items. Please make new order" )

        self.set_quantity(self.quantity - quantity)
        return quantity * self.price
