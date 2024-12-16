import carparking as cp

cpm = cp.CarParkingMachine(id="North", capacity=2, hourly_rate=4.0)
cpm.check_in("BB-494-H")
cpm.check_in("HH-494-B")

print(cpm.parked_cars)