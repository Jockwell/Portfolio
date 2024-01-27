'''Library Management System'''

import sqlite3

# Connecting to a database
db = sqlite3.connect('library_db')
print("Connection Established!")

# Creating a cursor object to allow for SQL commands to be connected.
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        title TEXT NOT NULL UNIQUE,
                                        author TEXT,
                                        genre TEXT,
                                        copies INTEGER NOT NULL);            

''')
db.commit()
print("Table Created!")


def insert_book():
    '''Function to insert a book into the database'''
    title = input("Please enter the book title : ")
    author = input("Please enter the author of the book : ")
    genre = input("Please enter the genre of the book : ")
    copies = int(input("Please enter the amount of copies for this book : "))

    cursor.execute('''
        INSERT INTO books (title, author, genre, copies)
                    VALUES(?,?,?,?);
    ''', (title, author, genre, copies))

    db.commit()
    print("Book has been inserted!")

def view_book():
    '''Function to view all books in the database'''
    cursor.execute('''
        SELECT * FROM books
    ''')

    all_book = cursor.fetchall()
    print(all_book)

menu = input('''
Welcome to the Library Database! Please make a menu selection below!
    1 - Add a new book to the database
    2 - Edit a book in the database
    3 - Manage inventory
    4 - check books being borrowed
    5 - Exit
''')

if menu == "1":
    insert_book()
elif menu == "3":
    view_book()
