import json  # Import the json module for working with JSON data

def translation(word):  # Define a function called translation that takes a word as input
    if word in data:  # Check if the word is present in the data dictionary
        print(data[word])  # If the word is found, print its translation
    else:
        print("data is not available")  # If the word is not found, print a message

if __name__ == '__main__':  # Check if the script is being run directly
    file = open("data.json")  # Open the data.json file
    data = json.load(file)  # Load the contents of the file into the data variable as a dictionary

    word = input("enter word: ")  # Prompt the user to enter a word
    translation(word)  # Call the translation function with the entered word as an argument
