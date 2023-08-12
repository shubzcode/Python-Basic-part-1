import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Simple Calculator")
label.pack()

entry_1 = tk.Entry(root)
entry_1.pack()

entry_2 = tk.Entry(root)
entry_2.pack()

button_add = tk.Button(
    root, text="Add", command=lambda: add_numbers(entry_1.get(), entry_2.get())
)
button_add.pack()

button_subtract = tk.Button(
    root,
    text="Subtract",
    command=lambda: subtract_numbers(entry_1.get(), entry_2.get()),
)
button_subtract.pack()

button_multiply = tk.Button(
    root,
    text="Multiply",
    command=lambda: multiply_numbers(entry_1.get(), entry_2.get()),
)
button_multiply.pack()

button_divide = tk.Button(
    root, text="Divide", command=lambda: divide_numbers(entry_1.get(), entry_2.get())
)
button_divide.pack()


def add_numbers(number_1, number_2):
    """Adds two numbers together."""
    sum = int(number_1) + int(number_2)
    label.config(text="The sum is: {}".format(sum))


def subtract_numbers(number_1, number_2):
    """Subtracts two numbers from each other."""
    difference = int(number_1) - int(number_2)
    label.config(text="The difference is: {}".format(difference))


def multiply_numbers(number_1, number_2):
    """Multiplies two numbers together."""
    product = int(number_1) * int(number_2)
    label.config(text="The product is: {}".format(product))


def divide_numbers(number_1, number_2):
    """Divides two numbers by each other."""
    quotient = int(number_1) // int(number_2)
    label.config(text="The quotient is: {}".format(quotient))


root.mainloop()
