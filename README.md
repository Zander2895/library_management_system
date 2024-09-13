Overview:

The Library Management System is a command-line application designed to manage library operations such as managing books, users, authors, and genres. It allows librarians or users to perform various operations including adding, borrowing, and returning books, as well as managing users, authors, and genres within the library.

This system is organized into different modules for better functionality and code readability. It now includes MySQL database integration for persistent data storage, ensuring that all operations are performed directly on the database, rather than using in-memory lists.

Features:

Main Menu:
Navigate to different operations such as book, user, author, and genre management.

Book:
Add a new book: Add a book to the library collection, which is stored in the database.
Borrow a book: Mark a book as borrowed by updating its availability status in the database.
Return a book: Mark a book as available by updating its status in the database.
Search for a book: Search for a book by its ISBN, retrieving information from the database.
Display all books: Display a list of all books stored in the database, along with their availability status.

User Operations:
Add a new user: Add a new user to the library system, storing user details in the database.
View user details: View a specific user's details, including their name and borrowed books, by querying the database.
Display all users: Display a list of all registered users from the database.

Author Operations:
Add a new author: Add a new author to the database.
View author details: View details of an author, including name and biography, by querying the database.
Display all authors: Display a list of all authors stored in the database.

Genre Operations:
Add a new genre: Add a new genre to categorize books, storing it in the database.
View genre details: View details of a genre, including name, description, and category, by querying the database.
Display all genres: Display a list of all genres stored in the database.

Database Integration:
The system is now integrated with a MySQL database, replacing in-memory lists with database queries. This ensures that all operations—adding, updating, deleting, and displaying records—are persistent and scalable. Each class (Book, User, Author, Genre) interacts directly with the database.

Database Tables:
The following tables are created to manage the data:

Books: Stores book information, including title, author ID, ISBN, and availability status.
Users: Stores user information, including name and library ID.
Authors: Stores author information, including name and biography.
Genres: Stores genre information, including name, description, and category.

MySQL Setup:
To set up the MySQL database, you will need to:

Install MySQL and set up a database.

Run the provided SQL script to create the necessary tables.

Update the database connection details (host, user, password, database) in the script.

How to Use:
Run the script using Python:
python library_management_system.py

Upon running, you will be presented with the Main Menu. From here, you can navigate to different sections:

Book Operations: Manage book-related activities.
User Operations: Manage users of the library.
Author Operations: Manage author-related data.
Genre Operations: Manage genre-related data.
Follow the on-screen prompts to perform various operations like adding new data, borrowing/returning books, updating records, and viewing existing data.

System Requirements:
Python 3.x or higher
MySQL (Installed and running)
Python modules:
mysql-connector-python (for MySQL database connection)
Custom modules: Book, User, Author, Genre (defined in separate files)

To install mysql-connector-python, run:
pip install mysql-connector-python

File Structure:
library_management_system.py: The main script containing the program logic and database operations.
book.py, user.py, author.py, genre.py: Custom modules where the Book, User, Author, and Genre classes are implemented.