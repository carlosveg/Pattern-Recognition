import tkinter as tk
from tkinter import messagebox

# Create the master object
master = tk.Tk()

master.geometry("300x300")

# Create a Scale Widget
scale_widget = tk.Scale(master, orient="horizontal", resolution=1,
                        from_=0, to=100)

# And a label for it
label_1 = tk.Label(master, text="Scale")

# Use the grid geometry manager to put the widgets in the respective position
label_1.grid(row=0, column=0)
scale_widget.grid(row=0, column=1)


def buttonCallback():
    global scale_widget
    messagebox.showinfo(
        "Message", "You have chosen value {}".format(scale_widget.get()))


button = tk.Button(master, text="Click", command=buttonCallback)
button.grid(row=1, column=1)

# The application mainloop
tk.mainloop()
