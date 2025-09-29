import tkinter
from tkinter import *

time_left = 5

def check_type():
    global time_left
    if time_left < 1:
        text = notes.get("1.0", END)
        window.clipboard_clear()
        window.clipboard_append(text)
        notes.delete("1.0", END)
        time_left = 5
        notes.edit_modified(True)
    if notes.edit_modified():
        time_left -= 1
    window.after(1000, check_type)


window = Tk()
window.title("The Most Dangerous Writing App")

window.configure(bg="#3A3A3A")
window.config(padx=50, pady=50)

title = Label(text="The Most Dangerous Writing App", font=("Helvetica", 60, "bold"), fg="#8B0000")
title.grid(column=0, row=0, pady=10)

notes = Text(height=30, width=100, bg="#3A3A3A",font=("Helvetica", 20))
notes.grid(column=0, row=1, padx=20, pady=10)

helper = Label(
    text="Don't worry: If you lost your work, it's on your clipboard.",
    font=("Helvetica", 8),
    fg="gray",
)
helper.grid(column=0, row=2, pady=10)
check_type()
window.mainloop()

