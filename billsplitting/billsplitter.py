import tkinter as tk

def calculate():
    try:
        num_roommates = int(num_roommates_entry.get())
        rent = float(rent_entry.get())
        utilities = float(utilities_entry.get())
        misc_exp = float(misc_exp_entry.get())

        total_bill = rent + utilities + misc_exp
        share = total_bill / num_roommates

        result_label.config(text="Each roommate owes: $" + str(share))
    except ValueError as e:
        result_label.config(text="Error: " + str(e))

# Create the GUI
root = tk.Tk()
root.title("Roommate Bill Splitting")

# Create the input fields
num_roommates_label = tk.Label(root, text="Number of Roommates:")
num_roommates_entry = tk.Entry(root)
rent_label = tk.Label(root, text="Rent:")
rent_entry = tk.Entry(root)
utilities_label = tk.Label(root, text="Utilities:")
utilities_entry = tk.Entry(root)
misc_exp_label = tk.Label(root, text="Miscellaneous Expenses:")
misc_exp_entry = tk.Entry(root)

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)

# Create the result label
result_label = tk.Label(root)

# Place the widgets on the screen
num_roommates_label.grid(row=0, column=0, sticky="w")
num_roommates_entry.grid(row=0, column=1, sticky="w")
rent_label.grid(row=1, column=0, sticky="w")
rent_entry.grid(row=1, column=1, sticky="w")
utilities_label.grid(row=2, column=0, sticky="w")
utilities_entry.grid(row=2, column=1, sticky="w")
misc_exp_label.grid(row=3, column=0, sticky="w")
misc_exp_entry.grid(row=3, column=1, sticky="w")
calculate_button.grid(row=4, column=1, sticky="w")
result_label.grid(row=5, column=0, columnspan=2, sticky="w")

root.mainloop()