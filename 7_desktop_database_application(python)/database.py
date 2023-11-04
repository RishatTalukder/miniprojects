# making the database and table to use in the application
import sqlite3


def connect():
    """
    Connects to the database and creates a table if it does not already exist.

    This function establishes a connection to the SQLite database file "books.db"
    located in the directory "7_desktop_database_application(python)". It then creates
    a table named "book" with the following columns: id (integer, primary key),
    title (text), author (text), year (integer), and isbn (integer). If the table
    already exists, this function does nothing.

    Parameters:
        None

    Returns:
        None
    """
    conn = sqlite3.connect("7_desktop_database_application(python)/books.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)"
    )

    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    """
    Inserts a new book into the database.

    Parameters:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The year the book was published.
        isbn (str): The ISBN of the book.

    Returns:
        None
    """
    conn = sqlite3.connect("7_desktop_database_application(python)/books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))

    conn.commit()
    conn.close()


def view():
    """
    Connects to a SQLite database and retrieves all rows from the "book" table.

    Returns:
        A list of tuples representing the rows retrieved from the database.
    """
    conn = sqlite3.connect("7_desktop_database_application(python)/books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


def delet(id=None, title=None, author=None, year=None, isbn=None, deletall=False):
    """
    Deletes a book from the database based on the provided parameters.

    Parameters:
        id (int): The ID of the book to delete.
        title (str): The title of the book to delete.
        author (str): The author of the book to delete.
        year (int): The year of publication of the book to delete.
        isbn (str): The ISBN of the book to delete.

    Returns:
        None
    """
    if id or title or author or year or isbn:
        conn = sqlite3.connect("7_desktop_database_application(python)/books.db")
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM book WHERE id=? or title=? or author=? or year=? or isbn=?",
            (id, title, author, year, isbn),
        )
        conn.commit()
        conn.close()

    # deleting all the books
    if deletall:
        conn = sqlite3.connect("7_desktop_database_application(python)/books.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM book")
        conn.commit()
        conn.close()


def search(title=None, author=None, year=None, isbn=None):
    """
    Searches for books in the database based on the provided parameters.

    Parameters:
        title (str): The title of the book to search for.
        author (str): The author of the book to search for.
        year (int): The year of publication of the book to search for.
        isbn (str): The ISBN of the book to search for.

    Returns:
        A list of tuples representing the rows retrieved from the database.
    """
    conn = sqlite3.connect("7_desktop_database_application(python)/books.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM book WHERE title=? or author=? or year=? or isbn=?",
        (title, author, year, isbn),
    )
    rows = cur.fetchall()
    conn.close()
    return rows


def update(id, title, author, year, isbn):
    """
    Updates a book record in the database with the given ID.

    Parameters:
        id (int): The ID of the book record to update.
        title (str): The new title of the book.
        author (str): The new author of the book.
        year (int): The new year of publication of the book.
        isbn (str): The new ISBN of the book.

    Returns:
        None
    """
    conn = sqlite3.connect("7_desktop_database_application(python)/books.db")
    cur = conn.cursor()
    cur.execute(
        "UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",
        (title, author, year, isbn, id),
    )
    conn.commit()
    conn.close()
