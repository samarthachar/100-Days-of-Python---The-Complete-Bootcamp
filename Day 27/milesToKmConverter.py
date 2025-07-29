from tkinter import *

window = Tk()
window.config(pady=20, padx=20)
window.title("Miles to Km Converter")

def change(inp):
    inp = int(inp)
    return str(round(inp * 1.60934))

def button_clicked():
    in_km = change(input_text.get())
    number.config(text=in_km)


input_text = Entry(width=10)
input_text.grid(column=1,row=0)
input_text.insert(END, "0")

miles = Label(text="Miles")
miles.grid(column=2, row=0)


is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

number = Label(text="0")
number.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)


calculate = Button(text="Calculate", command=button_clicked)
calculate.grid(column=1, row=2)




window.mainloop()