# PABUNA, KATRINA B. 
# BSCPE 1-4

# import tkinter
from tkinter import *
from tkinter import ttk

# main window
main = Tk()
main.title("COVID Contact Tracing App")
main.geometry("500x200")

# create a frame inside a window
widget = ttk.Frame(main)
widget.pack()

# personal information
user_info = ttk.Labelframe(widget, text="Personal Information")
user_info.grid(row=0, column=0)

# first name
first_name_label = ttk.Label(user_info, text="First Name:")
first_name_label.grid(row=0, column=0)

# COVID details
# add entry

# create a frame for data
# search entry

# ====== start ======
main.mainloop()