
trip = float(input("Distance traveled: "))

# Function to calculate the fare based on the distance traveled


def calculate_fare(distance):
    base_fare = 4.00  # Base fare in EUR
    fare_per_140 = 0.25  # Fare for every 140 meters
    distance_in_meters = distance * 1000  # Convert kilometers to meters
    total_fare = base_fare + (distance_in_meters / 140) * fare_per_140
    # Round to 2 decimal places for correct currency format
    return round(total_fare, 2)


# Interact with the user
if __name__ == "__main__":
    trip = float(input("Distance traveled (in km): "))
    print(f"Total fare: {calculate_fare(trip)} EUR")
