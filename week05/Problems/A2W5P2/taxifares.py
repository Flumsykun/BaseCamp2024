
trip = float(input("Distance traveled: "))

# Function to calculate the fare for a given distance


def calculate_fare(distance):
    base_fare = 4.00
    fare_per_140 = 0.25
    distance_in_meters = distance * 1000 # convert kilometers to meters


if __name__ == "__main__":
    print(f"Total fare: {calculate_fare(trip):.2f} EUR")
