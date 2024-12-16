import unittest
from datetime import datetime, timedelta
from carparking import CarParkingMachine, ParkedCar
import os


class TestCarParkingMachine(unittest.TestCase):
    def setUp(self):
        if os.path.exists("carparklog.txt"):
            os.remove("carparklog.txt")
        self.parking_machine = CarParkingMachine("test_machine", capacity=2, hourly_rate=2.50)

    def test_check_in_success(self):
        """Test a successful car check-in."""
        result = self.parking_machine.check_in("AA-123-B")
        self.assertTrue(result)
        self.assertIn("AA-123-B", self.parking_machine.parked_cars)

    def test_check_in_capacity_reached(self):
        """Test check-in fails when capacity is reached."""
        self.parking_machine.check_in("AA-123-B")
        self.parking_machine.check_in("BB-456-C")
        result = self.parking_machine.check_in("CC-789-D")
        self.assertFalse(result)

    def test_check_in_duplicate_license_plate(self):
        """Test check-in fails for a duplicate license plate."""
        self.parking_machine.check_in("AA-123-B")
        result = self.parking_machine.check_in("AA-123-B")
        self.assertFalse(result)

    def test_check_out_success(self):
        """Test a successful check-out with fee calculation."""
        check_in_time = datetime.now() - timedelta(hours=3)
        self.parking_machine.check_in("AA-123-B", check_in=check_in_time)
        fee = self.parking_machine.check_out("AA-123-B")
        self.assertAlmostEqual(fee, 7.50, places=2)

    def test_fee_capped_at_24_hours(self):
        """Test fee is capped at 24 hours."""
        check_in_time = datetime.now() - timedelta(days=2)
        self.parking_machine.check_in("AA-123-B", check_in=check_in_time)
        fee = self.parking_machine.get_parking_fee("AA-123-B")
        self.assertAlmostEqual(fee, 24 * 2.50, places=2)

    def test_fee_round_up_partial_hour(self):
        """Test parking fee rounds up for partial hours."""
        check_in_time = datetime.now() - timedelta(hours=2, minutes=15)
        self.parking_machine.check_in("AA-123-B", check_in=check_in_time)
        fee = self.parking_machine.get_parking_fee("AA-123-B")
        self.assertAlmostEqual(fee, 7.50, places=2)

    def test_get_parking_fee(self):
        """Test parking fee calculation."""
        check_in_time = datetime.now() - timedelta(hours=5, minutes=30)
        self.parking_machine.check_in("AA-123-B", check_in=check_in_time)
        fee = self.parking_machine.get_parking_fee("AA-123-B")
        self.assertAlmostEqual(fee, 15.00, places=2)

    def test_parking_machine_capacity(self):
        """Test the initial capacity of the parking machine."""
        self.assertEqual(self.parking_machine.capacity, 2)

    def test_hourly_rate(self):
        """Test the initial hourly rate of the parking machine."""
        self.assertEqual(self.parking_machine.hourly_rate, 2.50)


class TestParkedCar(unittest.TestCase):
    def test_parked_car_initialization(self):
        """Test initialization of a ParkedCar object."""
        check_in_time = datetime.now()
        car = ParkedCar("AA-123-B", check_in_time)
        self.assertEqual(car.license_plate, "AA-123-B")
        self.assertEqual(car.check_in, check_in_time)


if __name__ == "__main__":
    unittest.main()
