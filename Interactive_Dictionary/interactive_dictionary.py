import json
from difflib import SequenceMatcher, get_close_matches

# dictionary containing words and definitions
data = json.load(open("data.json"))

def get_word():
    """Returns a word taken from input."""
    word = input('Enter a word to lookup: ')
    return word


def get_matches(word):
    """Returns word(s) that closely matches the input."""
    closest_words = get_close_matches(word, data.keys())
    for item in get_close_matches(word, closest_words):
        print(item + '?')

def get_definition(word = None):
    """Prints English definitions for input word."""
    while word != False:
        word = get_word()

        if word == 'q':
            print('Exiting Program.')
            break

        word = word.lower()

        try:
            print(data[word][0])
        except KeyError:
            print("Word not found. Did you mean: ")
            get_matches(word)
            continue

def main():
    get_definition()

if __name__ == "__main__":
    main()
