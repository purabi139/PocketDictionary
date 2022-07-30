from colorama import Fore  # for colorful text in the terminal
from PocketDictionary import *


def execute():
    word = input(Fore.GREEN + 'Enter a word: ')

    try:
        meanings = PocketDictionary.get_word_meanings(word)
        if type(meanings) == list:
            for item in meanings:
                print(Fore.MAGENTA + item)
        else:
            print(meanings)
    except Exception as e:
        print(Fore.RED + str(e))

    choice = input(Fore.BLUE + '\nDo you want to search another word. Press Y or N: ')

    if choice.lower() == "y":
        execute()
    elif choice.lower() == "n":
        print(Fore.CYAN + "Thank you!!")
    else:
        print(Fore.CYAN + "We didn't understand your choice.", choice, "Exiting !!")


execute()
