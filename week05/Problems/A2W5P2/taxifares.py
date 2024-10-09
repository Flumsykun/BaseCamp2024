# Function to calculate the fare based on the distance traveled
def calculate_fare(distance):
    distance_meters = distance * 1000
    amount = 0
    fare = 4  # Start with the base fare

    while distance_meters > 0:
        amount += 1
        distance_meters -= 140
        fare = 4 + amount * 0.25

    print(f"Total fare: {round(fare, 2)} EUR")


if __name__ == "__main__":
    distance = float(input("Enter distance traveled: "))
    calculate_fare(distance)
