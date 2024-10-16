# Functions to add a book to the list

def add_book(books: list, book_details):
    title, author, publisher, pub_date = [
        x.strip() for x in book_details.split(",")]
    for book in books:
        if book['title'].lower() == title.lower():
            print("Book already exists.")
            return
    books.append({
        "title": title,
        "author": author,
        "publisher": publisher,
        "pub_date": pub_date
    })
    print("Book has been added.")

# Function to search for a book based on a term


def search_book(books, term):
    term = term.lower()
    for book in books:
        if term in book['title'].lower() or term in book['author'].lower() or term in book['publisher'].lower():
            print(f"Found a book for: {term}")
            return True
    print(f"No book found for: {term}")
    return False

# Main function for the menu


def main():
    books = []

    while True:
        print("\nMenu: [A] Add book [S] Search book [E] Exit (and print)")
        choice = input("Choose an option: ").upper()

        if choice == "A":
            book_details = input(
                "Enter book details (title, author, publisher, pub_date): ")
            add_book(books, book_details)

        elif choice == "S":
            term = input("Search term: ")
            search_book(books, term)

        elif choice == "E":
            print("\nExiting and printing all books...")
            for book in books:
                print(book)
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
