import tkinter as tk
from tkinter import *


root = Tk()

# Configure window
root.title("Currency Exchange Calculator")
root.geometry("400x300")

def calculate_exchange_rate():
    # get the input values
    amount = float(amount_entry.get())
    exchange_rate = float(rate_entry.get())

    # calculate the result
    result = amount * exchange_rate

    # display the result
    result_label.config(text=str(result))

# Create labels
amount_label = Label(root, text="Amount:")
rate_label = Label(root, text="Exchange Rate:")
result_label = Label(root, text="Result:")

# Create entry widgets
amount_entry = Entry(root)
rate_entry = Entry(root)

# Create button to perform calculation
calculate_button = Button(root, text="Calculate", command=calculate_exchange_rate)

# Grid layout
amount_label.grid(row=0, column=0, sticky=W)
amount_entry.grid(row=0, column=1)

rate_label.grid(row=1, column=0, sticky=W)
rate_entry.grid(row=1, column=1)

calculate_button.grid(row=2, column=0, columnspan=2)

result_label.grid(row=3, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()