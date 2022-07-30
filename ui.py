import tkinter as tk
from functools import partial
from PocketDictionary import *


def find_word_meanings(label_result, word_input):
    meanings = PocketDictionary.get_word_meanings(word_input.get())
    result = ''
    if type(meanings) == list:
        for meaning in meanings:
            result = result + meaning + "\n"
    else:
        result = meanings

    label_result.config(text="Below Meaning \n %s" % result)
    return


root = tk.Tk()
root.geometry('400x200+100+200')

root.title('Pocket Dictionary')

word_input = tk.StringVar()

tk.Label(root, text="Enter a word").grid(row=1, column=0)

labelResult = tk.Label(root)

labelResult.grid(row=7, column=0)

tk.Entry(root, textvariable=word_input).grid(row=1, column=2)

btn_action = partial(find_word_meanings, labelResult, word_input)

tk.Button(root, text="Find", command=btn_action).grid(row=3, column=0)

root.mainloop()
