from datetime import datetime
import math


class CarParkingMachine:
    def __init__(self, id, capacity=10, hourly_rate=2.50):
        """Initialize the parking machine with a machine ID, capacity, and hourly rate."""
        self.machine_id = id
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = {}  # Tracks cars: {license_plate: ParkedCar object}
        self.logger = CarParkingLogger(id)  # Initialize logger
        self.load_parked_cars()  # Load non-checked-out cars from the log file

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
        self.logger.log_check_out(license_plate, fee)  # Log the check-out
        del self.parked_cars[license_plate]  # Remove car
        return fee

    def load_parked_cars(self):
        """Load non-checked-out cars from the log file."""
        try:
            with open(self.logger.log_file, "r") as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split(";")
                    if len(parts) >= 4:
                        action = parts[3].split("=")[1]
                        if action == "check-in":
                            license_plate = parts[2].split("=")[1]
                            if license_plate not in self.parked_cars:
                                check_in_time = datetime.strptime(parts[0], "%d-%m-%Y %H:%M:%S")
                                self.parked_cars[license_plate] = ParkedCar(license_plate, check_in_time)
                        elif action == "check-out":
                            license_plate = parts[2].split("=")[1]
                            if license_plate in self.parked_cars:
                                del self.parked_cars[license_plate]  # Remove checked-out cars
        except FileNotFoundError:
            # Log file doesn't exist yet; no cars to load
            pass

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


class CarParkingLogger:
    def __init__(self, machine_id):
        """Initialize the logger with a machine ID."""
        self.machine_id = machine_id
        self.log_file = "carparklog.txt"

    def log_check_in(self, license_plate):
        """Log a car check-in."""
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        log_entry = f"{timestamp};cpm_name={self.machine_id};license_plate={license_plate};action=check-in\n"
        with open(self.log_file, "a") as f:
            f.write(log_entry)

    def log_check_out(self, license_plate, parking_fee):
        """Log a car check-out."""
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        log_entry = f"{timestamp};cpm_name={self.machine_id};license_plate={license_plate};action=check-out;parking_fee={parking_fee}\n"
        with open(self.log_file, "a") as f:
            f.write(log_entry)

    def get_machine_fee_by_day(self, search_date):
        """Calculate the total parking fee for this machine on a specific day."""
        total_fee = 0.0
        search_date = datetime.strptime(search_date, "%d-%m-%Y").date()
        with open(self.log_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split(";")
                if len(parts) >= 5:
                    timestamp = datetime.strptime(parts[0], "%d-%m-%Y %H:%M:%S")
                    machine_id = parts[1].split("=")[1]
                    if machine_id.lower() == self.machine_id.lower() and timestamp.date() == search_date:
                        action = parts[3].split("=")[1]
                        if action == "check-out":
                            fee = float(parts[4].split("=")[1])
                            total_fee += fee
        return round(total_fee, 2)

    def get_total_car_fee(self, license_plate):
        """Calculate the total fee for a specific car across all machines."""
        total_fee = 0.0
        with open(self.log_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split(";")
                if len(parts) >= 5:
                    plate = parts[2].split("=")[1]
                    if plate == license_plate:
                        action = parts[3].split("=")[1]
                        if action == "check-out":
                            fee = float(parts[4].split("=")[1])
                            total_fee += fee
        return round(total_fee, 2)

def main_menu():
    try:
        machine_id = input("Enter the parking machine ID: ").strip()
        parking_machine = CarParkingMachine(machine_id)

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
    except EOFError:
        print("\nNo input provided. Exiting program.")


if __name__ == "__main__":
    main_menu()