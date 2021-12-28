import tkinter as tk

screen = tk.Tk()
screen.title("Mile to KM Converter")
screen.minsize(width=300, height=100)
screen.config(padx=30, pady=30)


def calculate():
    miles = int(user_input.get())
    km = miles * 1.609
    calc_label.config(text=f"{km}")


user_input = tk.Entry()
user_input.grid(column=1, row=0)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

equals_label = tk.Label(text="is equal to")
equals_label.grid(column=0, row=1)

calc_label = tk.Label(text="")
calc_label.grid(column=1, row=1)

km_label = tk.Label(text="KM")
km_label.grid(column=2, row=1)

calc_button = tk.Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=2)

screen.mainloop()
