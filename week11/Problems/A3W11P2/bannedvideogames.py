import os
import sys
import csv


# Load the csv file
def load_data(filename):
    with open("bannedvideogames.csv", "r") as file:
        reader = csv.DictReader(file)
        print(reader.fieldnames)
        return list(reader)

# Save the csv file
def save_data(filename: str, data: list) -> None:
    with open("bannedvideogames.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(data)


# Count banned games in israel
def count_banned_in_israel(data):
    return sum(1 for game in data if game['Country'] == 'Israel')


# count country with the most bans
def country_with_most_bans(data: list) -> dict:
    country_count = {}
    for game in data:
        country = game['Country']
        country_count[country] = country_count.get(country, 0) + 1
    return max(country_count, key=country_count.get)


# Count how many Assassin's Creed games are banned
def count_assassins_creed_banned(data: list) -> int:
    banned_games = set()
    for game in data:
        if game['Series'] == ['Assassin\'s Creed']:
            banned_games.add(game['Title'])
        return len(banned_games)


# Show all games banned in germany
def games_banned_in_germany(data: list) -> list:
    return [game for game in data if game['Country'] == 'Germany']

# Show all games in banned in Australia
def games_banned_in_australia(data: list) -> list:
    return [game for game in data if game['Country'] == 'Australia']

# Show all countries where Red Dead Redemption is banned
def red_dead_banned_details(data: list) -> list:
    return [game for game in data if game['Game'] == 'Red Dead Redemption']


# Game modification extras
def remove_germany_records(data: list) -> list:
    return [game for game in data if game['Country'] != 'Germany']


# Rename Silent Hill VI to Silent Hill Remastered
def rename_silent_hill(data):
    for game in data:
        if game['Game'] == 'Silent Hill VI':
            game['Game'] = 'Silent Hill Remastered'


# Lift the ban on Bully in Brazil
def lift_bully_ban(data):
    for game in data:
        if game['Name'] == 'Bully' and game['Country'] == 'Brazil':
            game['Status'] = 'Ban Lifted'


# Change the genre of Manhunt II to Action
def change_manhunt_genre(data):
    for game in data:
        if game['Name'] == 'Manhunt II':
            game['Genre'] = 'Action'


# Add a new game to the list
def add_new_game(data):
    keys = ['id', 'name', 'series', 'country', 'details', 'category', 'status', 'wikipedia', 'image', 'summary',
            'developer', 'publisher', 'genre', 'homepage']
    new_game = {key: input(f"Enter {key}: ") for key in keys}
    data.append(new_game)


# Overview of Banned Games per Country
def overview_by_country(data):
    country_games = {}
    for game in data:
        country = game['country']
        if country not in country_games:
            country_games[country] = []
        country_games[country].append(game['name'])

    for country, games in country_games.items():
        print(f"{country} - {len(games)}")
        for game in games:
            print(f"- {game}")


# Search the dataset by country
def search_by_country(data, country):
    for game in data:
        if game['country'].lower() == country.lower():
            print(f"{game['name']} - {game['details']}")


def main():
    filename = 'bannedvideogames.csv'
    data = load_data(filename)

    while True:
        print("[I] Print request info from assignment")
        print("[M] Make modification based on assignment")
        print("[A] Add new game to list")
        print("[O] Overview of banned games per country")
        print("[S] Search the dataset by country")
        print("[Q] Quit program")

        choice = input("Enter your choice: ").strip().upper()

        if choice == 'I':
            print(f"Games banned in Israel: {count_banned_in_israel(data)}")
            print(f"Country with most bans: {country_with_most_bans(data)}")
            print(f"Assassin's Creed games banned: {count_assassins_creed_banned(data)}")
            print("Games banned in Germany:")
            for game in games_banned_in_germany(data):
                print(game)
            print("Red Dead Redemption banned details:")
            for game in red_dead_banned_details(data):
                print(game)
        elif choice == 'M':
            data = remove_germany_records(data)
            rename_silent_hill(data)
            lift_bully_ban(data)
            change_manhunt_genre(data)
            save_data(filename, data)
        elif choice == 'A':
            add_new_game(data)
            save_data(filename, data)
        elif choice == 'O':
            overview_by_country(data)
        elif choice == 'S':
            country = input("Enter country to search: ")
            search_by_country(data, country)
        elif choice == 'Q':
            save_data(filename, data)
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
