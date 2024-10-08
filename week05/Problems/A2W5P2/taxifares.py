
trip = float(input("Distance traveled: "))

# Function to calculate the fare for a given distance


def calculate_fare(distance):
    base_fare = 4.00  # base fare in EUR
    fare_per_140 = 0.25  # fare for every 140 meters
    distance_in_meters = distance * 1000  # convert kilometers to meters
    fare = base_fare + (distance_in_meters / 140) * fare_per_140
    return round(fare, 2)  # rounding to match expected output precision


# Main block to handle user input and show the fare
if __name__ == "__main__":
    trip = float(input("Distance traveled: "))
    print(f"Total fare: {calculate_fare(trip):.2f} EUR")
