import os
import sys


def load_txt_file(file_name):
    """Laadt de temperaturen van een tekstbestand in een gestructureerd formaat."""
    temperatures_for_year = {}
    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as file_obj:
        for line in file_obj.readlines():
            month, day, year, temperature = line.split()  # unpack into 4 variables
            year = int(year)
            month = int(month)
            temperature = float(temperature)

            if year not in temperatures_for_year:
                temperatures_for_year[year] = {}
            if month not in temperatures_for_year[year]:
                temperatures_for_year[year][month] = []

            temperatures_for_year[year][month].append(temperature)

    return temperatures_for_year


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Zet Fahrenheit om naar Celsius."""
    return (fahrenheit - 32) * 5 / 9


def average_temp_per_month(temperatures_for_year: dict) -> list:
    """Bereken de gemiddelde temperatuur per maand."""
    averages = []
    for month, temps in temperatures_for_year.items():
        averages.append((month, sum(temps) / len(temps)))
        return averages


def average_temp_per_year(temperatures: dict) -> list:
    """Bereken de gemiddelde temperatuur per jaar."""
    yearly_averages = []
    for year, months in temperatures.items():
        total_temp = sum(sum(temps) for temps in months.values())
        total_days = sum(len(temps) for temps in months.values())
        avg_temp = total_temp / total_days
        yearly_averages.append((year, round(avg_temp, 2)))
    return yearly_averages


def warmest_and_coldest_year(temperatures: dict) -> tuple:
    """Vind het warmste en koudste jaar op basis van de gemiddelde temperatuur."""
    yearly_averages = average_temp_per_year(temperatures)
    warmest_year = max(yearly_averages, key=lambda x: x[1])
    coldest_year = min(yearly_averages, key=lambda x: x[1])
    return warmest_year, coldest_year


def warmest_month_of_year(temperatures: dict, year: int) -> str:
    """Vind de warmste maand van een bepaald jaar."""
    if year in temperatures:
        avg_temps = average_temp_per_month(temperatures[year])
        warmest_month = max(avg_temps, key=lambda x: x[1])[0]
        return month_name(warmest_month)
    else:
        return "Year not found."


def coldest_month_of_year(temperatures: dict, year: int) -> str:
    """Vind de koudste maand van een bepaald jaar."""
    if year in temperatures:
        avg_temps = average_temp_per_month(temperatures[year])
        coldest_month = min(avg_temps, key=lambda x: x[1])[0]
        return month_name(coldest_month)


def month_name(month_num: int) -> str:
    """Geef de volledige maandnaam op basis van een maandnummer."""
    return ["January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"][month_num - 1]


def average_temp_month_per_year(temperatures: dict) -> list:
    """Print een lijst van jaren met maandelijkse gemiddelde temperaturen in Celsius."""
    result = []
    for year, months in temperatures.items():
        month_averages = {month_name(month): fahrenheit_to_celsius(sum(temps) / len(temps))
                          for month, temps in months.items()}
        result.append((year, month_averages))
        return result


def main_menu(temperatures):
    """Hoofdmenu voor gebruikersinterface"""
    while True:
        print("\n[1] Print average temperatures per year (Fahrenheit)")
        print("[2] Print average temperatures per year (Celsius)")
        print("[3] Print the warmest and coldest year based on the average temperature")
        print("[4] Print the warmest month of a year")
        print("[5] Print the coldest month of a year")
        print("[6] Print average temperatures per month in Celsius")
        print("[Q] Quit")

        while True:
            choice = input("Choose an option: ").upper()
            if choice in ['1', '2', '3', '4', '5', '6', 'Q']:
                break
            else:
                print("Invalid option. Please try again.")

        if choice == '1':
            yearly_averages = average_temp_per_year(temperatures)
            for year, avg_temp in yearly_averages:
                print(f"{year}: {avg_temp:.2f}°F")
        elif choice == '2':
            yearly_averages = average_temp_per_year(temperatures)
            for year, avg_temp in yearly_averages:
                print(f"{year}: {fahrenheit_to_celsius(avg_temp):.2f}°C")
        elif choice == '3':
            warmest, coldest = warmest_and_coldest_year(temperatures)
            print(
                f"Warmest year: {warmest[0]} with average {warmest[1]:.2f}°F")
            print(
                f"Coldest year: {coldest[0]} with average {coldest[1]:.2f}°F")
        elif choice == '4':
            year = int(input("Enter the year: "))
            print(
                f"Warmest month in {year}: {warmest_month_of_year(temperatures, year)}")
        elif choice == '5':
            year = int(input("Enter the year: "))
            print(
                f"Coldest month in {year}: {coldest_month_of_year(temperatures, year)}")
        elif choice == '6':
            result = average_temp_month_per_year(temperatures)
            for year, month_avg in result:
                print(f"{year}: {month_avg}")
        elif choice == 'Q':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == '__main__':
    temperatures = load_txt_file('NLAMSTDM.txt')
    main_menu(temperatures)
