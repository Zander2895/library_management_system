Overview:

The Library Management System is a command-line application designed to manage the operations of a library, such as managing books, users, authors, and genres. It allows librarians or users to perform various operations including adding, borrowing, and returning books, as well as managing users, authors, and genres within the library.

This system is organized into different modules for better functionality and code readability. It incorporates operations like adding new books, users, authors, and genres, searching for books, viewing details, and more.

Features:

The program provides the following functionalities:

Main Menu

Navigate to different operations such as book, user, author, and genre management.
Book Operations

Add a new book to the library collection.
Borrow a book (mark it as borrowed).
Return a book (mark it as available).
Search for a book by its ISBN.
Display all books with their availability status.
User Operations

Add a new user to the system.
View details of a specific user (name and borrowed books).
Display all users in the system.
Author Operations

Add a new author to the library's records.
View details of an author, including name and biography.
Display all authors.
Genre Operations

Add a new genre to categorize books.
View details of a genre, including name, description, and category.
Display all genres.

How to Use:

Run the script using Python:
python library_management_system.py

Upon running, you will be presented with the Main Menu. From here, you can navigate to different sections:

Book Operations: Manage book-related activities.
User Operations: Manage users of the library.
Author Operations: Manage author-related data.
Genre Operations: Manage genre-related data.
Follow the on-screen prompts to perform various operations like adding new data, borrowing/returning books, and viewing existing data.

System Requirements:

Python 3.x or higher
Modules: re, Book, User, Author, Genre (custom modules defined in separate files)

File Structure:

library_management_system.py: The main script containing the program logic.
book.py, user.py, author.py, genre.py: Custom modules where the Book, User, Author, and Genre classes are implemented.