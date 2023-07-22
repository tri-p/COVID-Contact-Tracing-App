# PABUNA, KATRINA B. 
# BSCPE 1-4

# import tkinter
from tkinter import *
from tkinter import ttk

import csv

# main window
class Application(Tk):
    def __init__(self):
        super().__init__()
        self.title("COVID Contact Tracing App")
        self.configure(bg="#B2BEB5")
    
    # def add_entry function
        def add_entry():
            # open the csv file and write data
                with open("details.csv", "a", newline="") as details:
                    write = csv.writer(details)
                    write.writerow([first_name_entry.get(), last_name_entry.get(),
                                   self.vax_var.get(), self.exp_var.get(), self.test_var.get()])

    # create a frame inside a window
        widget = ttk.Frame(self)
        widget.pack(padx=20, pady=15)

    # personal information
        user_info = ttk.Labelframe(widget, text="Personal Information")
        user_info.grid(row=0, column=0, padx=20, pady=10, sticky=EW)

        # first name
        first_name_label = ttk.Label(user_info, text="First Name:")
        first_name_label.grid(row=0, column=0, padx=10, pady=5)

        first_name_entry = ttk.Entry(user_info)
        first_name_entry.grid(row=0, column=1, padx=(5, 10), pady=(0, 5))

        # last name
        last_name_label = ttk.Label(user_info, text="Last Name:")
        last_name_label.grid(row=1,column=0, padx=10, pady=(0, 10))

        last_name_entry = ttk.Entry(user_info)
        last_name_entry.grid(row=1,column=1, padx=(5, 10), pady=(0, 10))

    # COVID details
        covid_details = ttk.Labelframe(widget, text="COVID Details")
        covid_details.grid(row=1, column=0, padx=20, pady=(0, 10))

        # vaccination status
        vax_status_list = ["Not Vaccinated", "Vaccinated - 1st Dose", "Vaccinated - 2nd Dose", 
                           "Vaccinated - 1st Booster", "Vaccinated - 2nd Booster"]
        self.vax_var = StringVar(self)

        vax_label = ttk.Label(covid_details, text="Please select your vaccination status:")
        vax_label.grid(row=0, column=0, padx=10, pady=(5, 0), sticky=EW)

        vax_opt = ttk.OptionMenu(covid_details, self.vax_var, *vax_status_list)
        vax_opt.configure(direction="below")
        vax_opt.grid(row=1, column=0, padx=10, pady=(0, 10), sticky=EW)

        # exposure to COVID
        self.exp_var = StringVar(self)

        exposure_label = ttk.Label(covid_details, text="Have you had exposure to a probable or \nconfirmed case in the last 14 days?")
        exposure_label.grid(row=2, column=0, padx=10, sticky=EW)

        exp_rdbtn1 = ttk.Radiobutton(covid_details, text="Yes", variable=self.exp_var, value="Yes")
        exp_rdbtn1.grid(row=3, column=0, padx=10, sticky=EW)

        exp_rdbtn2 = ttk.Radiobutton(covid_details, text="No", variable=self.exp_var, value="No")
        exp_rdbtn2.grid(row=4, column=0, padx=10, sticky=EW)

        exp_rdbtn3 = ttk.Radiobutton(covid_details, text="Uncertain", variable=self.exp_var, value="Uncertain")
        exp_rdbtn3.grid(row=5, column=0, padx=10, sticky=EW)

        # tested for COVID
        self.test_var = StringVar(self)

        tested_label = ttk.Label(covid_details, text="Have you been tested for COVID-19\nin the last 14 days?")
        tested_label.grid(row=6, column=0, padx=10, pady=(10, 0), sticky=EW)

        test_rdbtn1 = ttk.Radiobutton(covid_details, text="No", variable=self.test_var, value="No")
        test_rdbtn1.grid(row=7, column=0, padx=10, sticky=EW)

        test_rdbtn2 = ttk.Radiobutton(covid_details, text="Yes - Positive", variable=self.test_var, value="Yes - Positive")
        test_rdbtn2.grid(row=8, column=0, padx=10, sticky=EW)

        test_rdbtn3 = ttk.Radiobutton(covid_details, text="Yes - Negative", variable=self.test_var, value="Yes - Negative")
        test_rdbtn3.grid(row=9, column=0, padx=10, sticky=EW)

        test_rdbtn4 = ttk.Radiobutton(covid_details, text="Yes - Pending", variable=self.test_var, value="Yes - Pending")
        test_rdbtn4.grid(row=10, column=0, padx=10, pady=(0, 5), sticky=EW)

    # add entry
        submit_btn = ttk.Button(widget, text="Submit", command=add_entry)
        submit_btn.grid(row=2, column=0, padx=20, pady=(0, 10))

        # search entry