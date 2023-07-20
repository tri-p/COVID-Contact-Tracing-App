# PABUNA, KATRINA B. 
# BSCPE 1-4

# import tkinter
from tkinter import *
from tkinter import ttk

# main window
main = Tk()
main.title("COVID Contact Tracing App")
main.geometry("400x175")

# create a frame inside a window
widget = ttk.Frame(main)
widget.pack()

# personal information
user_info = ttk.Labelframe(widget, text="Personal Information")
user_info.grid(row=0, column=0, padx=20, pady=10)

# first name
first_name_label = ttk.Label(user_info, text="First Name:")
first_name_label.grid(row=0, column=0, padx=10, pady=(5, 0), sticky=EW)

first_name_entry = ttk.Entry(user_info)
first_name_entry.grid(row=1, column=0, padx=10, pady=(0, 5), sticky=EW)

last_name_label = ttk.Label(user_info, text="Last Name:")
last_name_label.grid(row=2,column=0, padx=10, sticky=EW)

last_name_entry = ttk.Entry(user_info)
last_name_entry.grid(row=3,column=0, padx=10, pady=(0, 5), sticky=EW)

# COVID details
# add entry

# create a frame for data
# search entry

# ====== start ======
main.mainloop()