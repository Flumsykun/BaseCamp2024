class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, amount):
        if amount < 10:
            price = amount * self.price
        elif amount < 99:
            price = amount * self.price
            price = price * 0.9
        else:
            price = amount * self.price
            price = price * 0.8

        return price

    def print(self):
        print(f"Name: {self.name}")
        print(f"Amount: {self.amount}")
        print(f"Price: {self.price}")

    def make_purchase(self, amount):
        self.amount -= amount

    def get_amount(self):
        return self.amount

    def get_name(self):
        return self.name

