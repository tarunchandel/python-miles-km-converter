import tkinter as tk


def add(*args):
    total = 0
    for num in args:
        total += num
    return total


def calc(num, **kwargs):
    output = num
    if kwargs.get("add") is None:
        kwargs.__setitem__("add", 0)
    if kwargs.get("multiply") is None:
        kwargs.__setitem__("multiply", 1)
    output += kwargs.get("add")
    output *= kwargs.get("multiply")
    return output


screen = tk.Tk()
screen.title("My GUI")
screen.minsize(width=500, height=300)

my_label = tk.Label(text=f"The output is: ", font=("Arial", 24, "normal"))
my_label.pack()


def button_click():
    mult = calc(23, add=5, multiply=23)
    addition = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    my_label.config(text=f"Mult: {mult} | Add: {addition}\n{my_entry.get()}")


my_button = tk.Button(text="My Button", command=button_click)
my_button.pack()

my_entry = tk.Entry()
my_entry.pack()
my_entry.insert(tk.END, "Type anything")
my_entry.focus()

screen.mainloop()
