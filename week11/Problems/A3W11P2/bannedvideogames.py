import csv
import os


def load_data(filename):
    with open(filename, "r", newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)


def save_data(filename, data):
    fieldnames = ['Id', 'Game', 'Series', 'Country', 'Details', 'Ban Category',
                  'Ban Status', 'Wikipedia Profile', 'Image', 'Summary', 'Developer',
                  'Publisher', 'Genre', 'Homepage']
    sanitized_data = []
    for row in data:
        sanitized_row = {key: row.get(key, "") for key in fieldnames}
        sanitized_data.append(sanitized_row)

    with open(filename, "w", newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sanitized_data)


def count_banned_in_israel(data):
    return sum(1 for game in data if game['Country'].lower() == 'israel')


def country_with_most_bans(data):
    country_count = {}
    for game in data:
        country = game['Country']
        country_count[country] = country_count.get(country, 0) + 1
    return max(country_count, key=country_count.get)


def count_assassins_creed_banned(data):
    return len({game['Game'] for game in data if game['Series'].lower() == "assassin's creed"})


def games_banned_in_germany(data):
    return [game for game in data if game['Country'].lower() == 'germany']


def red_dead_banned_details(data):
    return [game for game in data if game['Game'].lower() == 'red dead redemption']


def remove_germany_records(data):
    return [game for game in data if game['Country'].lower() != 'germany']


def rename_silent_hill(data):
    for game in data:
        if game['Game'].lower() == 'silent hill vi':
            game['Game'] = 'Silent Hill Remastered'


def lift_bully_ban(data):
    for game in data:
        if game['Game'].lower() == 'bully' and game['Country'].lower() == 'brazil':
            game['Ban Status'] = 'Ban Lifted'


def change_manhunt_genre(data):
    for game in data:
        if game['Game'].lower() == 'manhunt ii':
            game['Genre'] = 'Action'


def add_new_game(data):
    fieldnames = ['Id', 'Game', 'Series', 'Country', 'Details', 'Ban Category', 'Ban Status', 'Wikipedia Profile',
                  'Image', 'Summary', 'Developer', 'Publisher', 'Genre', 'Homepage']
    new_game = {field: input(f"Enter {field}: ") for field in fieldnames}
    data.append(new_game)


def overview_by_country(data):
    country_games = {}
    for game in data:
        country = game['Country']
        country_games.setdefault(country, []).append(game['Game'])
    for country, games in country_games.items():
        print(f"{country} - {len(games)}")
        for game in games:
            print(f"- {game}")


def search_by_country(data, country):
    results = [game for game in data if game['Country'].lower() == country.lower()]
    for game in results:
        print(f"{game['Game']} - {game['Details']}")


def main():
    filename = 'bannedvideogames.csv'
    if not os.path.exists(filename):
        print("File not found.")
        return

    game_data = load_data(filename)

    while True:
        print("[I] Print request info from assignment")
        print("[M] Make modification based on assignment")
        print("[A] Add new game to list")
        print("[O] Overview of banned games per country")
        print("[S] Search the dataset by country")
        print("[Q] Quit program")

        choice = input("Enter your choice: ").strip().upper()

        if choice == 'I':
            print(count_banned_in_israel(game_data))
            print(country_with_most_bans(game_data))
            print(count_assassins_creed_banned(game_data))

            saudi_games = [game for game in game_data if 'saudi' in game['Country'].lower()]
            emirates_games = [game for game in game_data if 'emirates' in game['Country'].lower()]

            for game in saudi_games:
                print(f"{game['Game']} - {game['Details']}")
            for game in emirates_games:
                print(f"{game['Game']} - {game['Details']}")
        elif choice == 'M':
            game_data = remove_germany_records(game_data)
            rename_silent_hill(game_data)
            lift_bully_ban(game_data)
            change_manhunt_genre(game_data)
            save_data(filename, game_data)
        elif choice == 'A':
            add_new_game(game_data)
            save_data(filename, game_data)
        elif choice == 'O':
            overview_by_country(game_data)
        elif choice == 'S':
            country = input("Enter country to search: ")
            search_by_country(game_data, country)
        elif choice == 'Q':
            save_data(filename, game_data)
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()