class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def set_quantity(self, quantity):
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def show(self):
        print(self.name + ", Price: " + str(self.price) + ", Quantity: " + str(self.quantity))

    def buy(self, quantity):
        if quantity > self.quantity:
            raise ValueError("Not enough " + self.name + "in store. We have only " + str(self.quantity) + " items. Please make new order" )
        else:
            self.set_quantity(self.quantity - quantity)
            return quantity * self.price


