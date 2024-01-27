import tkinter as tk
from tkinter import messagebox
import datetime

def send_notification(root):
    # Get the selected hour and minute from the global variables
    selected_hour = int(hour_var.get())
    selected_minute = int(minute_var.get())

    # Get the current time
    now = datetime.datetime.now()

    # Create a datetime object for the selected time today
    alarm_time = now.replace(hour=selected_hour, minute=selected_minute, second=0, microsecond=0)

    # Calculate the time to wait until the alarm
    time_to_wait = (alarm_time - now).total_seconds()

    if time_to_wait > 0:
        #print(f"Scheduled notification in {time_to_wait} seconds...")
        root.after(int(time_to_wait * 1000), lambda: show_alert(root))  # Convert seconds to milliseconds

def show_alert(root):
    # Get the message from the Entry widget
    message = message_entry.get()

    # Show the notification using Tkinter's messagebox
    messagebox.showinfo("Notification", message)

def gui():
    global hour_var, minute_var, message_entry  # Declare global variables

    root = tk.Tk()
    root.title("Notification Timer")
    root.geometry("500x300")

    # Create a label frame for the time and message
    time_message_frame = tk.LabelFrame(root, text="Notification Settings", font=("Arial", 20))
    time_message_frame.grid(row=0, column=0, padx=20, pady=20)

    # Create a label for the time
    time_label = tk.Label(time_message_frame, text="Time:", font=("Arial", 20))
    time_label.grid(row=0, column=0, padx=20, pady=20)

    # Create a drop-down menu for the hour
    hour_var = tk.StringVar(root)
    hour_var.set('Hour')
    hour_menu = tk.OptionMenu(time_message_frame, hour_var, *range(24))
    hour_menu.config(width=5)
    hour_menu.grid(row=0, column=1, padx=20, pady=20)

    # Create a drop-down menu for the minute
    minute_var = tk.StringVar(root)
    minute_var.set('Minute')
    minute_menu = tk.OptionMenu(time_message_frame, minute_var, *range(60))
    minute_menu.config(width=5)
    minute_menu.grid(row=0, column=2, padx=20, pady=20)

    # Create a label for the message
    message_label = tk.Label(time_message_frame, text="Message:", font=("Arial", 20))
    message_label.grid(row=1, column=0, padx=20, pady=20)

    # Create a text entry for the message
    message_entry = tk.Entry(time_message_frame)
    message_entry.grid(row=1, column=1, columnspan=2, padx=20, pady=20)

    # Create a button to trigger the notification
    enter_button = tk.Button(root, text='Enter', font=("Arial", 10), command=lambda: send_notification(root))
    enter_button.grid(row=2, column=0, padx=20, pady=20)

    root.mainloop()

gui()