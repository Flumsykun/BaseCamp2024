import os
import sys
import json


def load_movies():
    """Load movies from the JSON file."""
    if os.path.exists("movies.json"):
        with open("movies.json", "r") as file:
            return json.load(file)
    return []


class MovieManager:
    def __init__(self):
        self.movies = load_movies()

    def save_movies(self):
        """Save movies back to the JSON file."""
        with open("movies.json", "w") as file:
            json.dump(self.movies, file, indent=4)

    def display_movie_info(self):
        """Display movie-related queries."""
        count_2004 = sum(1 for movie in self.movies if movie["year"] == 2004)
        sci_fi_count = sum(1 for movie in self.movies if "Science Fiction" in movie["genres"])
        keanu_movies = [movie for movie in self.movies if "Keanu Reeves" in movie["cast"]]
        stallone_movies = [
            movie for movie in self.movies
            if "Sylvester Stallone" in movie["cast"] and 1995 <= movie["year"] <= 2005
        ]

        print(f"Movies released in 2004: {count_2004}")
        print(f"Movies in Science Fiction genre: {sci_fi_count}")
        print("Movies with Keanu Reeves:", keanu_movies)
        print("Movies with Sylvester Stallone (1995-2005):", stallone_movies)

    def modify_movies(self):
        """Modify movie data as per the assignment."""
        for movie in self.movies:
            if movie["title"] == "Gladiator":
                movie["year"] = 2001

        oldest_movie = min(self.movies, key=lambda m: m["year"])
        oldest_movie["year"] -= 1

        for movie in self.movies:
            if "Natalie Portman" in movie["cast"]:
                movie["cast"] = [
                    "Nat Portman" if actor == "Natalie Portman" else actor
                    for actor in movie["cast"]
                ]
            if "Kevin Spacey" in movie["cast"]:
                movie["cast"].remove("Kevin Spacey")

    def search_movie(self, title):
        """Search for a movie by title."""
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                print(movie)
                return
        print("Movie not found.")

    def change_movie_details(self, title, new_title, new_year):
        """Change a movie's title and/or release year."""
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                movie["title"] = new_title
                movie["year"] = new_year
                print("Movie updated:", movie)
                return
        print("Movie not found.")


def main():
    manager = MovieManager()

    while True:
        print("[I] Movie information overview")
        print("[M] Make modification based on assignment")
        print("[S] Search a movie title ")
        print("[C] Change title and/or release year by search on title")
        print("[Q] Quit program")

        choice = input("Enter your choice: ").strip().upper()

        if choice == "I":
            manager.display_movie_info()
        elif choice == "M":
            manager.modify_movies()
        elif choice == "S":
            title = input("Enter movie title to search: ").strip()
            manager.search_movie(title)
        elif choice == "C":
            title = input("Enter movie title to change: ").strip()
            new_title = input("Enter new title: ").strip()
            new_year = int(input("Enter new release year: ").strip())
            manager.change_movie_details(title, new_title, new_year)
        elif choice == "Q":
            manager.save_movies()
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()