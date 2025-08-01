from tkinter import *
import pandas
import random
#------------------------------------Constants------------------------------------#
BACKGROUND_COLOR = "#B1DDC6"

current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")


#------------------------------------Create New Flash Cards------------------------------------#

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_label, text="French", fill="black")
    canvas.itemconfig(word_label, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, flip_card)
#------------------------------------Flip the Cards------------------------------------#
def flip_card():
    canvas.itemconfig(title_label, fill="white", text="English")
    canvas.itemconfig(word_label, fill="white",text=current_card["English"])
    canvas.itemconfig(card_background, image = card_back_img)
#------------------------------------Save your Progress------------------------------------#
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
#------------------------------------Graphical User Interface------------------------------------#

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0,row=0, columnspan=2)

title_label = canvas.create_text(400,150,text="title", font=("Ariel", 40, "italic"))

word_label = canvas.create_text(400,263,text="word", font=("Ariel", 60, "bold"))

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0,row=1)


right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=is_known)
right_button.grid(column=1,row=1)

next_card()

window.mainloop()
