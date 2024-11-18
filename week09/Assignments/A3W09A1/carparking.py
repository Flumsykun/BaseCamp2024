import math
from datetime import datetime


class CarParkingMachine:
    def __init__(self, capacity=10, hourly_rate=2.50):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = {}  # Tracks cars: {license_plate: ParkedCar object}

    def check_in(self, license_plate, check_in=None):
        """Register a car's entry if capacity isn't reached."""
        if len(self.parked_cars) >= self.capacity:
            return False  # Capacity reached
        if license_plate in self.parked_cars:
            return False  # Car already checked in
        if check_in is None:
            check_in = datetime.now()
        self.parked_cars[license_plate] = ParkedCar(license_plate, check_in)
        return True  # Successfully checked in

    def check_out(self, license_plate):
        """Register a car's departure and calculate parking fee."""
        if license_plate not in self.parked_cars:
            return None  # Car not found
        fee = self.get_parking_fee(license_plate)
        del self.parked_cars[license_plate]  # Remove car
        return fee

    def get_parking_fee(self, license_plate):
        """Calculate and return the parking fee for a car."""
        if license_plate not in self.parked_cars:
            return None  # Car not found
        parked_car = self.parked_cars[license_plate]
        now = datetime.now()
        parked_duration = now - parked_car.check_in
        parked_hours = math.ceil(parked_duration.total_seconds() / 3600)  # Round up to nearest hour
        parked_hours = min(parked_hours, 24)  # Cap at 24 hours
        return round(parked_hours * self.hourly_rate, 2)  # Fee rounded to 2 decimals


class ParkedCar:
    def __init__(self, license_plate, check_in):
        """Represents a parked car."""
        self.license_plate = license_plate
        self.check_in = check_in


def main_menu():
    parking_machine = CarParkingMachine()

    while True:
        print("\nMenu:")
        print("[I] Check-in car by license plate")
        print("[O] Check-out car by license plate")
        print("[Q] Quit program")
        choice = input("Choose an option: ").strip().upper()

        if choice == "I":
            license_plate = input("License: ").strip()
            if parking_machine.check_in(license_plate):
                print("License registered")
            else:
                if len(parking_machine.parked_cars) >= parking_machine.capacity:
                    print("Capacity reached!")
                else:
                    print("License already checked in!")

        elif choice == "O":
            license_plate = input("License: ").strip()
            fee = parking_machine.check_out(license_plate)
            if fee is None:
                print(f"License {license_plate} not found!")
            else:
                print(f"Parking fee: {fee:.2f} EUR")

        elif choice == "Q":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main_menu()
