from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
front = ""
back = ""
words_to_remove = []
language_dict = {}

window = Tk()
window.title("flash card project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


def flip_card():
    canvas.itemconfig(language, text="English", fill="white")
    global back
    canvas.itemconfig(vocabulary, text=back, fill="white")

    canvas.itemconfig(canvas_image, image=card_img_back)
    window.after(3000, select_word)


flip_timer = window.after(3000, flip_card)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img_front = PhotoImage(file="./images/card_front.png")
card_img_back = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_img_front)

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    # language_dict = original_data.to_dict(orient="records")
    language_dict = {row.French: row.English for (index, row) in original_data.iterrows()}
else:
    language_dict = {row.French: row.English for (index, row) in data.iterrows()}





def select_word():
    # print(language_dict)
    random_french_word = str(choice(list(language_dict)))
    english_translation = language_dict[random_french_word]
    global front, back, flip_timer
    window.after_cancel(flip_timer)
    front = random_french_word
    back = english_translation
    canvas.itemconfig(vocabulary, text=front, fill="black")
    canvas.itemconfig(language, text="French", fill="black")
    flip_timer = window.after(3000, flip_card)


language = canvas.create_text(400, 150, text="French", font=(FONT_NAME, 40, "italic"))
vocabulary = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)



wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=select_word)
wrong_button.grid(column=0, row=1)


def remove_word():
    global front
    try:
        language_dict.pop(front)
    except KeyError:
        pass
    data_to_read = pandas.DataFrame.from_dict(language_dict, orient="index")
    data_to_read.to_csv("./data/words_to_learn.csv")


right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=remove_word)
right_button.grid(column=1, row=1)

select_word()

window.mainloop()

