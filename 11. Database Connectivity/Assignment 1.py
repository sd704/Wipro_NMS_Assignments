# Task 1: Write a Python script that connects to an SQLite3 database file,
# creates a table books with columns title, author, and year,
# and inserts multiple rows of data into the table.

# Task 2: Extend the previous SQLite3 task by adding functionality to
# select a book by title, update the author of a book,
# and delete a book from the books table.


import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


host_name = "localhost"
user_name = "root"
user_password = "Password@1"
db_name = "training"
connection = create_connection(host_name, user_name, user_password, db_name)

create_books_table_query = """
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    PRIMARY KEY (id)
) ENGINE = InnoDB
"""

books_to_insert = [
    ('The Great Gatsby', 'F. Scott Fitzgerald', 1925),
    ('To Kill a Mockingbird', 'Harper Lee', 1960),
    ('1984', 'George Orwell', 1949),
    ('Pride and Prejudice', 'Jane Austen', 1813),
    ('The Catcher in the Rye', 'J.D. Salinger', 1951)
]

insert_books_query = """
INSERT INTO books (title, author, year) VALUES (%s, %s, %s)
"""


def execute_query(connection, query, data=None):
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as e:
        print(f"The error '{e}' occurred")


# Creating the table and inserting data
execute_query(connection, create_books_table_query)
for book in books_to_insert:
    execute_query(connection, insert_books_query, book)


def fetch_query(connection, query, data=None):
    cursor = connection.cursor(dictionary=True)
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        result = cursor.fetchone()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
        return None


def select_book_by_title(connection, title):
    select_query = f'SELECT * FROM books WHERE title = "{title}"'
    return fetch_query(connection, select_query)


print("Selecting '1984': \n", select_book_by_title(connection, '1984'))


def update_book_author(connection, title, new_author):
    update_query = f'UPDATE books SET author = "{new_author}" WHERE title = "{title}"'
    execute_query(connection, update_query)


print("Before updating '1984': \n", select_book_by_title(connection, '1984'))
update_book_author(connection, '1984', 'George')
print("Updated '1984': \n", select_book_by_title(connection, '1984'))


def delete_book_by_title(connection, title):
    delete_query = f'DELETE FROM books WHERE title = "{title}"'
    execute_query(connection, delete_query)


print("Before deleting '1984': \n", select_book_by_title(connection, '1984'))
delete_book_by_title(connection, '1984')
print("Deleted '1984': \n", select_book_by_title(connection, '1984'))

# Close the connection
if connection.is_connected():
    connection.close()
    print("MySQL connection is closed")

