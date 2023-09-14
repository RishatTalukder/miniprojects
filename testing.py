import sqlite3

conn = sqlite3.connect("dictionary copy.db")  # creating a connection to the database
cursor = conn.cursor()  # cursor object created to perform operations on the database

cursor.execute(
    "select Word from Dictionary"
)
word_list = cursor.fetchall()
word_list = [word[0] for word in word_list]

print(word_list)