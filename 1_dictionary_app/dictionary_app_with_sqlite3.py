from difflib import (
    get_close_matches,
)  # importing difflib which gives the closest matches of a string
import sqlite3


conn = sqlite3.connect(
    "1_dictionary_app/dictionary.db"
)  # creating a connection to the database
cursor = conn.cursor()  # cursor object created to perform operations on the database


word_list = cursor.execute(
    "select Word from Dictionary"
).fetchall()  # getting all the words from the database
word_list = [word[0] for word in word_list]  # converting the list of tuples to a list


def translate(w):
    """
    Translates a word into its meaning.

    Args:
        w (str): The word to be translated.

    Returns:
        list[str]: A list of meanings of the word. If the word is not found in the data,
        it prompts the user for a possible alternative suggestion using difflib.get_close_matches().

    Raises:
        None.
    """
    w = w.lower()  # transfroming the word to lowercase because it is case sensitive

    if w in word_list:  # checking if the word is in the data
        meaning = cursor.execute(
            "select Definition from Dictionary where Word = ?", (w,)
        ).fetchall()  # getting the meaning
        meaning = [
            mean[0] for mean in meaning
        ]  # converting the list of tuples to a list
        return meaning  # returning the translation

    elif len(get_close_matches(w, word_list)) > 0:  # if the word is not in the data
        """
        If the word is not in the data, the function prompts the user for a possible
        alternative suggestion. by using difflib.get_close_matches()
        """
        close_matches = get_close_matches(w, word_list)
        yn = input(
            "Did you mean %s instead? Enter Y if yes, or N if no: " % close_matches[0]
        )

        if yn == "Y" or yn == "y":  # if the user confirms the suggestions
            meaning = cursor.execute(
                "select Definition from Dictionary where Word = ?", (close_matches[0],)
            ).fetchall()  # getting the meaning
            meaning = [
                mean[0] for mean in meaning
            ]  # converting the list of tuples to a list
            return meaning  # returning the translation

        elif yn == "N" or yn == "n":  # if the user rejects the suggestions
            return "The word doesn't exist. Please double check it."

        else:
            return "We didn't understand your entry."

    else:
        return "The word doesn't exist. Please double check it."


if __name__ == "__main__":
    word = input("Enter word: ")  # taking input
    output = translate(word)  # calling the translate function
    if type(output) == list:  # if the output is a list
        for item in output:  # iterating through the list
            print(item)
    else:
        print(output)
