import os
import sys
import csv


def load_csv_file(file_name):
    file_content = []
    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as csv_file:
        file_content = list(csv.DictReader(csv_file, delimiter=","))
    return file_content


def get_headers(file_content):
    return list(next(iter(file_content)).keys())


def search_by_type(file_content, show_type):
    return [show for show in file_content if show['type'] == show_type]


def count_by_type(file_content):
    num_tv_shows = len(search_by_type(file_content, 'TV Show'))
    num_movies = len(search_by_type(file_content, 'Movie'))
    print(f"TV Shows: {num_tv_shows}")
    print(f"Movies: {num_movies}")


def get_directors(file_content):
    directors = set()
    for row in file_content:
        if row['director']:
            directors.add(row['director'])
    return directors


def directors_with_both(file_content):
    directors = get_directors(file_content)
    both_directors = []

    for director in directors:
        director_shows = search_by_director(file_content, director)
        movies = search_by_type(director_shows, 'Movie')
        tv_shows = search_by_type(director_shows, 'TV Show')

        if movies and tv_shows:
            both_directors.append(director.title())

    return sorted(both_directors)


def search_by_director(file_content, director):
    return list(filter(lambda x: x['director'] == director, file_content))


def director_counts(file_content):
    directors = get_directors(file_content)
    results = []

    for director in directors:
        movies = search_by_type(search_by_director(file_content, director), 'Movie')
        tv_shows = search_by_type(search_by_director(file_content, director), 'TV Show')
        results.append((director, len(movies), len(tv_shows)))

    return sorted(results, key=lambda x: x[1] + x[2], reverse=True)[:5]


def main():
    file_name = 'netflix_titles.csv'  # Hardcoded filename
    file_content = load_csv_file(file_name)

    choice = input("Enter your choice: ")
    if choice == '1':
        print(f"TV Shows: {len(search_by_type(file_content, 'TV Show'))}")
    elif choice == '2':
        print(f"Movies: {len(search_by_type(file_content, 'Movie'))}")
    elif choice == '3':
        both_directors = directors_with_both(file_content)
        print("[", end="")
        for i, director in enumerate(both_directors):
            print(f"'{director}'", end=", " if i < len(both_directors) - 1 else "")
        print("]")
    elif choice == '4':
        director_counts_list = director_counts(file_content)
        for director, movie_count, tv_show_count in director_counts_list[:10]:
            print(f"{director}: {movie_count} movies, {tv_show_count} TV shows")
    elif choice.upper() == 'Q':
        print("Exiting program.")
    else:
        print("Invalid option, try again.")


if __name__ == '__main__':
    main()
