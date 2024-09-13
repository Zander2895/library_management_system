import re
import mysql.connector

from book import Book
from user import User
from author import Author
from genre import Genre

books = []
users = []
authors = []
genres = []

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1:3306",
            user="root",
            password="1Y6%11]5?16f",
            database="Library_Management_System"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


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

def add_book():
    title = input("Enter the title of the book: ")
    author_id = input("Enter the author ID: ")
    isbn = input("Enter the ISBN of the book: ")
    publication_date = input("Enter the publication date of the book (YYYY-MM-DD): ")

    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO Books (title, author_id, isbn, publication_date) VALUES (%s, %s, %s, %s)"
        values = (title, author_id, isbn, publication_date)
        cursor.execute(query, values)
        connection.commit()
        print(f"Book '{title}' added successfully!")
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")


def borrow_book():
    isbn = input("Enter the ISBN of the book to borrow: ")

    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "SELECT title, is_available FROM Books WHERE isbn = %s"
        cursor.execute(query, (isbn,))
        result = cursor.fetchone()

        if result:
            title, is_available = result
            if is_available:
                update_query = "UPDATE Books SET is_available = FALSE WHERE isbn = %s"
                cursor.execute(update_query, (isbn,))
                connection.commit()
                print(f"You have borrowed '{title}'")
            else:
                print(f"'{title}' is already borrowed.")
        else:
            print("Book not found.")
        
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")


def return_book():
    isbn = input("Enter the ISBN of the book to return: ")

    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "SELECT title, is_available FROM Books WHERE isbn = %s"
        cursor.execute(query, (isbn,))
        result = cursor.fetchone()

        if result:
            title, is_available = result
            if not is_available:
                update_query = "UPDATE Books SET is_available = TRUE WHERE isbn = %s"
                cursor.execute(update_query, (isbn,))
                connection.commit()
                print(f"You have returned '{title}'")
            else:
                print(f"'{title}' was not borrowed.")
        else:
            print("Book not found.")
        
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")


def search_book():
    isbn = input("Enter the ISBN of the book to search: ")

    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "SELECT title, author_id, publication_date, is_available FROM Books WHERE isbn = %s"
        cursor.execute(query, (isbn,))
        result = cursor.fetchone()

        if result:
            title, author_id, publication_date, is_available = result
            availability = "Available" if is_available else "Borrowed"
            print(f"Title: {title}\nAuthor ID: {author_id}\nPublication Date: {publication_date}\nAvailability: {availability}")
        else:
            print("Book not found.")
        
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")


def display_books():
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "SELECT title, isbn, is_available FROM Books"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            for row in results:
                title, isbn, is_available = row
                availability = "Available" if is_available else "Borrowed"
                print(f"Title: {title}, ISBN: {isbn}, Availability: {availability}")
        else:
            print("No books available.")

        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")

def update_book():
    isbn = input("Enter the ISBN of the book to update: ")
    
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "SELECT * FROM Books WHERE isbn = %s"
        cursor.execute(query, (isbn,))
        result = cursor.fetchone()

        if result:
            new_title = input("Enter new title (leave blank to keep unchanged): ") or result[1]
            new_author_id = input("Enter new author ID (leave blank to keep unchanged): ") or result[2]
            new_publication_date = input("Enter new publication date (YYYY-MM-DD, leave blank to keep unchanged): ") or result[3]
            
            update_query = "UPDATE Books SET title = %s, author_id = %s, publication_date = %s WHERE isbn = %s"
            cursor.execute(update_query, (new_title, new_author_id, new_publication_date, isbn))
            connection.commit()
            print(f"Book '{isbn}' updated successfully!")
        else:
            print("Book not found.")
        
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")

def delete_book():
    isbn = input("Enter the ISBN of the book to delete: ")
    
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "DELETE FROM Books WHERE isbn = %s"
        cursor.execute(query, (isbn,))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"Book '{isbn}' deleted successfully!")
        else:
            print("Book not found.")
        
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")

def add_user():
    name = input("Enter the user's name: ")
    library_id = input("Enter the user's library ID: ")

    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO Users (name, library_id) VALUES (%s, %s)"
        values = (name, library_id)
        cursor.execute(query, values)
        connection.commit()
        print(f"User '{name}' added successfully!")
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")

def view_user_details():
    library_id = input("Enter the user's library ID: ")

    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "SELECT name FROM Users WHERE library_id = %s"
        cursor.execute(query, (library_id,))
        result = cursor.fetchone()

        if result:
            name = result[0]
            print(f"Name: {name}")
            # Fetch borrowed books (assumed a `borrowed_books` table for storing this relation)
            book_query = "SELECT b.title FROM Books b JOIN BorrowedBooks bb ON b.book_id = bb.book_id WHERE bb.user_id = (SELECT user_id FROM Users WHERE library_id = %s)"
            cursor.execute(book_query, (library_id,))
            borrowed_books = cursor.fetchall()
            if borrowed_books:
                print("Borrowed Books: " + ", ".join([book[0] for book in borrowed_books]))
            else:
                print("No borrowed books.")
        else:
            print("User not found.")
        
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")

def display_users():
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "SELECT name, library_id FROM Users"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            for row in results:
                name, library_id = row
                print(f"Name: {name}, Library ID: {library_id}")
        else:
            print("No users available.")

        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")

def update_user():
    library_id = input("Enter the library ID of the user to update: ")

    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "SELECT * FROM Users WHERE library_id = %s"
        cursor.execute(query, (library_id,))
        result = cursor.fetchone()

        if result:
            new_name = input("Enter new name (leave blank to keep unchanged): ") or result[1]
            
            update_query = "UPDATE Users SET name = %s WHERE library_id = %s"
            cursor.execute(update_query, (new_name, library_id))
            connection.commit()
            print(f"User '{library_id}' updated successfully!")
        else:
            print("User not found.")
        
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")

def delete_user():
    library_id = input("Enter the library ID of the user to delete: ")

    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "DELETE FROM Users WHERE library_id = %s"
        cursor.execute(query, (library_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"User '{library_id}' deleted successfully!")
        else:
            print("User not found.")
        
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")

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

def update_author():
    name = input("Enter the name of the author to update: ")

    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "SELECT * FROM Authors WHERE name = %s"
        cursor.execute(query, (name,))
        result = cursor.fetchone()

        if result:
            new_biography = input("Enter new biography (leave blank to keep unchanged): ") or result[1]
            
            update_query = "UPDATE Authors SET biography = %s WHERE name = %s"
            cursor.execute(update_query, (new_biography, name))
            connection.commit()
            print(f"Author '{name}' updated successfully!")
        else:
            print("Author not found.")
        
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")

def delete_author():
    name = input("Enter the name of the author to delete: ")

    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "DELETE FROM Authors WHERE name = %s"
        cursor.execute(query, (name,))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"Author '{name}' deleted successfully!")
        else:
            print("Author not found.")
        
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")

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

def update_genre():
    name = input("Enter the name of the genre to update: ")

    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "SELECT * FROM Genres WHERE name = %s"
        cursor.execute(query, (name,))
        result = cursor.fetchone()

        if result:
            new_description = input("Enter new description (leave blank to keep unchanged): ") or result[1]
            new_category = input("Enter new category (leave blank to keep unchanged): ") or result[2]
            
            update_query = "UPDATE Genres SET description = %s, category = %s WHERE name = %s"
            cursor.execute(update_query, (new_description, new_category, name))
            connection.commit()
            print(f"Genre '{name}' updated successfully!")
        else:
            print("Genre not found.")
        
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")

def delete_genre():
    name = input("Enter the name of the genre to delete: ")

    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "DELETE FROM Genres WHERE name = %s"
        cursor.execute(query, (name,))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"Genre '{name}' deleted successfully!")
        else:
            print("Genre not found.")
        
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")

if __name__ == "__main__":
    main_menu()