import json  # reads json file
from difflib import get_close_matches  # finds the closest match for a given word

# load the json data into dictionary
dictionary = json.loads(open('data/dictionary.json').read())

# generate available keys (a.k.a. words) in the dictionary
dictionary_keys = dictionary.keys()


class PocketDictionary:
    @staticmethod
    def get_word_meanings(word):
        word = word.lower()  # keys are in lower case

        if word in dictionary:
            return dictionary[word]

        # takes misspelled as first param and keys(words) as second param and returns the 1st closest matched word (if available)
        closest_matches = get_close_matches(word, dictionary_keys,
                                            1)
        if len(closest_matches) > 0:
            first_matched_word = closest_matches[0]

            choice = input("Did you mean %s instead? Enter Y if yes, otherwise N to exit: " % first_matched_word)

            if choice.lower() == "y":
                return dictionary[first_matched_word]
            elif choice.lower() == "n":
                raise Exception("The word " + word + " doesn't exist. Please double check it.")
            else:
                raise Exception("We didn't understand your choice " + choice)
        else:
            raise Exception("Sorry, this word " + word + " is not an English word. Please double check your spelling.")
