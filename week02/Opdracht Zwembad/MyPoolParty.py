# Het bedrijf MyPoolParty verkoopt allerei zwembaden die je in de zomer in je achtertuin kunt zetten.
# Hun helpdesk krijgt veel vragen over hoe lang het duurt om een zwembad met bepaalde afmetingen te vullen. 
# Maak een programma waarmee de medewerkers van de helpdesk dat makkelijk kunnen berekenen 
import math
def calculate_square_pool_volume(length, width, height):
    
    #   Calculate the volume of the swimming pool.
    
    # :param length: Length of the pool in meters.
    # :param width: Width of the pool in meters.
    # :param height: Height of the pool in meters.
    # :return: Volume of the pool in cubic meters.
    
    return length * width * height

def calculate_round_pool_volume(diameter, height):
    
    radius = diameter / 2
    return math.pi * (radius ** 2) * height

def convert_volume_to_liters(volume_m3):
    
    # Convert volume from cubic meters to liters.
    
    # :param volume_m3: Volume in cubic meters.
    # :return: Volume in liters.

    return volume_m3 * 1000

def calculate_fill_time(volume_liters, fill_rate_liters_per_hour):
    
    return volume_liters / fill_rate_liters_per_hour

def main():
    # Ask user for the shape of the pool
    shape = input("Is your pool square or round? (Enter 'square' or 'round'): ").strip().lower()
    
    if shape == 'square':
        # Input for square (rectangular) pool
        length = float(input("Enter the length of the pool in meters: "))
        width = float(input("Enter the width of the pool in meters: "))
        height = float(input("Enter the height of the pool in meters: "))
        
        # Calculate volume
        volume_m3 = calculate_square_pool_volume(length, width, height)
        
    elif shape == 'round':
        # Input for round pool
        diameter = float(input("Enter the diameter of the pool in meters: "))
        height = float(input("Enter the height of the pool in meters: "))
        
        # Calculate volume
        volume_m3 = calculate_round_pool_volume(diameter, height)
        
    else:
        print("Invalid shape. Please enter 'square' or 'round'.")
        return
    
    # Input for fill rate
    fill_rate = float(input("Enter the fill rate in liters per hour: "))
    
    # Convert volume to liters
    volume_liters = convert_volume_to_liters(volume_m3)
    
    # Calculate fill time
    time_hours = calculate_fill_time(volume_liters, fill_rate)
    
    # Output result
    print(f"The pool volume is {volume_liters:.2f} liters.")
    print(f"It will take approximately {time_hours:.2f} hours to fill the pool.")

if __name__ == "__main__":
    main()