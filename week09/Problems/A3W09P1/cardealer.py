class Car:
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.sold = False
        self.sold_to = None

    def sell(self, customer):
        self.sold = True
        self.sold_to = customer

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")
        print(f"Sold: {self.sold}")
        if self.sold:
            print(f"Sold to: {self.sold_to.name}")
        else:
            print("Status: Not sold yet")


class Motorcycle(Car):
    def __init__(self, brand, model, color, price):
        super().__init__(brand, model, color, price)


class Customer:
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Name: {self.name}")


if __name__ == "__main__":
    # Create a car and motorcycle
    car = Car("BMW", "X5", "Black", 34899)

    motorcycle = Motorcycle("Harley Davidson", "Iron 883", "Red", 12000)

    # Create a customer
    customer = Customer("Alice")

    # Sell car to the customer
    car.sell(customer)
    car.print()

    # Sell motorcycle to the same customer
    motorcycle.sell(customer)
    motorcycle.print()
