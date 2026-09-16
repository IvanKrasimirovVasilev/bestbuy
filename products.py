class Product:
    """Represent a product in the store."""

    def __init__(self, name, price, quantity):
        """Create a product."""
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details")

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
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def show(self):
        """Display the product information."""
        print(self.name + ", Price: " + str(self.price) +
              ", Quantity: " + str(self.quantity))

    def buy(self, quantity):
        """Buy a quantity of the product."""
        if quantity > self.quantity:
            raise ValueError("Not enough " + self.name +
                             "in store. We have only " + str(self.quantity) +
                             " items. Please make new order" )

        self.set_quantity(self.quantity - quantity)
        return quantity * self.price
