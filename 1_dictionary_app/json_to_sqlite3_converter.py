import json
import sqlite3


conn = sqlite3.connect("dictionary.db")  # creating a connection to the database
cursor = conn.cursor()  # cursor object created to perform operations on the database
cursor.execute(
    "Create table if not exists Dictionary (Word text, Definition text)"
)  # creating a table in the database

# loading the json data
data = json.load(open("data.json"))


# now to insert the data into the table
for (
    word,
    definition,
) in data.items():  # iterating through the dictionary data we got from the json file
    for i in definition:  # checking for evry meaning of the word
        cursor.execute(
            "insert into Dictionary values (?,?)", (word, i)
        )  # inserting the data
        print(f"-->{word}<-- Successfully inserted")

conn.commit()
conn.close()
