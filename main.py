import re
from book import Book
from user import User
from author import Author
from genre import Genre

books = []
users = []
authors = []
genres = []

def main_menu():
    while True:
        print("\nWelcome to the Library Management System!\n")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")

        choice = input("Select an option: ")

        if choice == '1':
            book_operations()
        elif choice == '2':
            user_operations()
        elif choice == '3':
            author_operations()
        elif choice == '4':
            genre_operations()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

def book_operations():
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            search_book()
        elif choice == '5':
            display_books()
        elif choice == '6':
            break
        else:
            print("Invalid option, please try again.")

def user_operations():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == '1':
            add_user()
        elif choice == '2':
            view_user_details()
        elif choice == '3':
            display_users()
        elif choice == '4':
            break
        else:
            print("Invalid option, please try again.")

def author_operations():
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == '1':
            add_author()
        elif choice == '2':
            view_author_details()
        elif choice == '3':
            display_authors()
        elif choice == '4':
            break
        else:
            print("Invalid option, please try again.")

def genre_operations():
    while True:
        print("\nGenre Operations:")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")
        print("4. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == '1':
            add_genre()
        elif choice == '2':
            view_genre_details()
        elif choice == '3':
            display_genres()
        elif choice == '4':
            break
        else:
            print("Invalid option, please try again.")

def validate_date(date_str):
    if re.match(r"\d{4}-\d{2}-\d{2}", date_str):
        return True
    return False

def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    isbn = input("Enter the ISBN of the book: ")
    publication_date = input("Enter the publication date of the book (YYYY-MM-DD): ")

    if not validate_date(publication_date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    new_book = Book(title, author, isbn, publication_date)
    books.append(new_book)
    print(f"Book '{title}' added successfully!")

def borrow_book():
    isbn = input("Enter the ISBN of the book to borrow: ")
    for book in books:
        if book.get_isbn() == isbn:
            if book.borrow():
                print(f"You have borrowed '{book.get_title()}'")
            else:
                print(f"'{book.get_title()}' is already borrowed.")
            return
    print("Book not found.")

def return_book():
    isbn = input("Enter the ISBN of the book to return: ")
    for book in books:
        if book.get_isbn() == isbn:
            if not book.is_available():
                book.return_book()
                print(f"You have returned '{book.get_title()}'")
            else:
                print(f"'{book.get_title()}' was not borrowed.")
            return
    print("Book not found.")

def search_book():
    isbn = input("Enter the ISBN of the book to search: ")
    for book in books:
        if book.get_isbn() == isbn:
            print(f"Title: {book.get_title()}\nAuthor: {book.get_author()}\nPublication Date: {book.get_publication_date()}\nAvailability: {'Available' if book.is_available() else 'Borrowed'}")
            return
    print("Book not found.")

def display_books():
    if not books:
        print("No books available.")
    for book in books:
        print(f"Title: {book.get_title()}, ISBN: {book.get_isbn()}, Availability: {'Available' if book.is_available() else 'Borrowed'}")

def add_user():
    name = input("Enter the user's name: ")
    library_id = input("Enter the user's library ID: ")

    if not re.match(r"^[a-zA-Z0-9]+$", library_id):
        print("Invalid library ID. Please use alphanumeric characters only.")
        return

    new_user = User(name, library_id)
    users.append(new_user)
    print(f"User '{name}' added successfully!")

def view_user_details():
    library_id = input("Enter the user's library ID: ")
    for user in users:
        if user.get_library_id() == library_id:
            print(f"Name: {user.get_name()}\nBorrowed Books: {', '.join(user.get_borrowed_books())}")
            return
    print("User not found.")

def display_users():
    if not users:
        print("No users available.")
    for user in users:
        print(f"Name: {user.get_name()}, Library ID: {user.get_library_id()}")

def add_author():
    name = input("Enter the author's name: ")
    biography = input("Enter the author's biography: ")
    new_author = Author(name, biography)
    authors.append(new_author)
    print(f"Author '{name}' added successfully!")

def view_author_details():
    name = input("Enter the author's name: ")
    for author in authors:
        if author.get_name() == name:
            print(f"Name: {author.get_name()}\nBiography: {author.get_biography()}")
            return
    print("Author not found.")

def display_authors():
    if not authors:
        print("No authors available.")
    for author in authors:
        print(f"Name: {author.get_name()}")

def add_genre():
    name = input("Enter the genre's name: ")
    description = input("Enter the genre's description: ")
    category = input("Enter the genre's category: ")
    new_genre = Genre(name, description, category)
    genres.append(new_genre)
    print(f"Genre '{name}' added successfully!")

def view_genre_details():
    name = input("Enter the genre's name: ")
    for genre in genres:
        if genre.get_name() == name:
            print(f"Name: {genre.get_name()}\nDescription: {genre.get_description()}\nCategory: {genre.get_category()}")
            return
    print("Genre not found.")

def display_genres():
    if not genres:
        print("No genres available.")
    for genre in genres:
        print(f"Name: {genre.get_name()}")

if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        print(f"An error occurred: {e}")
