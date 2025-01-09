import sqlite3
import math
import os
from datetime import datetime

class CarParkingMachine:
    all_parking_machines = []

    def __init__(self, id, capacity=10, hourly_rate=2.50):
        """Initialize the parking machine."""
        self.machine_id = id
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.db_conn = sqlite3.connect(os.path.join(os.getcwd(), 'carparkingmachine.db'))
        self.db_conn.execute(
            '''CREATE TABLE IF NOT EXISTS parkings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                car_parking_machine TEXT NOT NULL,
                license_plate TEXT NOT NULL,
                check_in TEXT NOT NULL,
                check_out TEXT DEFAULT NULL,
                parking_fee NUMERIC DEFAULT 0
            );'''
        )
        self.parked_cars = {}
        CarParkingMachine.all_parking_machines.append(self)

    def check_in(self, license_plate, check_in=None):
        """Check if a car can check-in and save state."""
        cursor = self.db_conn.cursor()
        cursor.execute(
            "SELECT id FROM parkings WHERE license_plate = ? AND check_out IS NULL",
            (license_plate,)
        )
        if cursor.fetchone():
            return False  # Car already checked in

        if len(self.parked_cars) >= self.capacity:
            return False  # Capacity reached

        check_in_time = check_in.strftime("%Y-%m-%d %H:%M:%S") if check_in else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            "INSERT INTO parkings (car_parking_machine, license_plate, check_in) VALUES (?, ?, ?)",
            (self.machine_id, license_plate, check_in_time),
        )
        self.db_conn.commit()
        self.parked_cars[license_plate] = ParkedCar(license_plate, datetime.strptime(check_in_time, "%Y-%m-%d %H:%M:%S"))
        return True

    def check_out(self, license_plate):
        """Check out a car, calculate fee, and save state."""
        cursor = self.db_conn.cursor()
        cursor.execute(
            "SELECT id, check_in FROM parkings WHERE license_plate = ? AND check_out IS NULL",
            (license_plate,)
        )
        row = cursor.fetchone()
        if not row:
            return None  # Car not found

        car_id, check_in_time = row
        check_in_time = datetime.strptime(check_in_time, "%Y-%m-%d %H:%M:%S")
        check_out_time = datetime.now()
        duration = check_out_time - check_in_time
        hours = math.ceil(duration.total_seconds() / 3600)
        fee = round(min(hours, 24) * self.hourly_rate, 2)

        cursor.execute(
            "UPDATE parkings SET check_out = ?, parking_fee = ? WHERE id = ?",
            (check_out_time.strftime("%Y-%m-%d %H:%M:%S"), fee, car_id),
        )
        self.db_conn.commit()
        if license_plate in self.parked_cars:
            del self.parked_cars[license_plate]
        return fee

    def get_active_parked_cars(self):
        """Retrieve all currently parked cars."""
        cursor = self.db_conn.cursor()
        cursor.execute(
            "SELECT license_plate FROM parkings WHERE check_out IS NULL AND car_parking_machine = ?",
            (self.machine_id,)
        )
        return cursor.fetchall()

def main_menu():
    parking_machine = CarParkingMachine("North")

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
                print("Capacity reached or already checked in!")

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

class ParkedCar:
    def __init__(self, license_plate, check_in):
        self.license_plate = license_plate
        self.check_in = check_in

if __name__ == "__main__":
    main_menu()