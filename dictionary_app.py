import json  # importing json
from difflib import (
    get_close_matches,
)  # importing difflib which gives the closest matches of a string

data = json.load(open("data.json"))  # opening the json file and loading it


def translate(w):
    """
    Translates a word into another language.

    Parameters:
    - w (str): The word to be translated.

    Returns:
    - str: The translated word. If the word is found in the data dictionary, the translation
           is returned. If the word is not found, the function prompts the user for a possible
           alternative suggestion. If the user confirms the suggestion, the translation is
           returned. If the user rejects the suggestion, a message indicating that the word
           doesn't exist is returned. If the user's input is not recognized, a message indicating
           that the input is not understood is returned.
    """
    w = w.lower()  # transfroming the word to lowercase because it is case sensitive
    if w in data:  # checking if the word is in the data
        return data[w]  # returning the translation
    elif len(get_close_matches(w, data.keys())) > 0:  # if the word is not in the data

        """
        If the word is not in the data, the function prompts the user for a possible
        alternative suggestion. by using difflib.get_close_matches()
        """

        close_matches = get_close_matches(w, data.keys())
        yn = input(
            "Did you mean %s instead? Enter Y if yes, or N if no: "
            % close_matches[0]
        )

        if yn == "Y" or yn == "y": # if the user confirms the suggestions
            return data[close_matches[0]] 
        elif yn == "N" or yn == "n": # if the user rejects the suggestions
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


if __name__ == "__main__":
    word = input("Enter word: ") # taking input
    output = translate(word) # calling the translate function 
    if type(output) == list: # if the output is a list
        for item in output: # iterating through the list 
            print(item)
    else:
        print(output)
