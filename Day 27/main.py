from tkinter import *
window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)


# Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "New text"
# Or
my_label.config(text="New Text")


#Button
def button_clicked():
    output = input.get()
    my_label.config(text=output)


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()

# Advanced Python Arguments

# Args
def add(n1, n2):
    return n1 + n2

def optimized_add(*args):#Could be named anything, only * is required
    # print(args[1])
    total = 0
    for n in args:
        total += n
    return total

# print(optimized_add(3,5,6))

# kwargs
def calculate(n, **kwargs):
    # print(kwargs)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)
calculate(2, add=3, multiply=5)





class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan")
# print(my_car.model)
window.mainloop()
