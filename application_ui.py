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
    
    # def clear_btn function
        def clear_btn_func():
            first_name_entry.delete(0, END)
            last_name_entry.delete(0, END)
            self.vax_var.set("(Select Vaccination Status)")
            self.exp_var.set("")
            self.test_var.set("")
    
    # def add_entry function
        def add_entry():
            # open the csv file and write data
            with open("details.csv", "a", newline="") as details:
                write = csv.writer(details)
                '''.capitalize() allows the user to input in any format in the name entry 
                and the program will get the data with auto-capitalized first letter'''
                write.writerow([first_name_entry.get().capitalize(), last_name_entry.get().capitalize(),
                                self.vax_var.get(), self.exp_var.get(), self.test_var.get()])

            # clearing the form after submitting an entry
            first_name_entry.delete(0, END)
            last_name_entry.delete(0, END)
            self.vax_var.set("(Select Vaccination Status)")
            self.exp_var.set("")
            self.test_var.set("")   

    # def search_btn function
        def search_entry_window():

            # def exit_btn function
            def exit_btn_func():
                search_entry.delete(0, END)
                search_entry_window.destroy()

            # def search_entry function
            def search_entry_func():
                # opening the csv file
                with open("details.csv") as file:
                    name = search_entry.get()
                    data = []

                    csv_reader = csv.reader(file)
                    for row in csv_reader:
                        data.append(row)

                    # only for the last name
                    row_set = []
                    row_set = [row[1].lower() for row in data] # converts the items in the list to lowercase

                    # finding the searched input in the list of last names
                    for row in range(0, len(data)):
                        for item in row_set:
                            if name.lower() == data[row][1].lower(): # converts the user's input to lowercase

                                # creating a frame to display the searched entry
                                disp_frame = ttk.Frame(search_entry_window)
                                disp_frame.grid(row=1, column=0, padx=20, pady=(0, 15))

                                # display the first name
                                disp_fname = ttk.Label(disp_frame, text="First Name: " + str(data[row][0]))
                                disp_fname.grid(row=0, column=0, padx=20)

                                # display the last name
                                disp_lname = ttk.Label(disp_frame, text="Last Name: " + str(data[row][1]))
                                disp_lname.grid(row=1, column=0, padx=20)

                                # display the vax status
                                disp_vax = ttk.Label(disp_frame, text="Vaccination Status: " + str(data[row][2]))
                                disp_vax.grid(row=2, column=0, padx=20)
                                
                                # display the answer to exposure
                                disp_exp = ttk.Label(disp_frame, text="Exposure to COVID: " + str(data[row][3]))
                                disp_exp.grid(row=3, column=0, padx=20)

                                # display the answer to COVID test
                                disp_test = ttk.Label(disp_frame, text="Tested for COVID: " + str(data[row][4]))
                                disp_test.grid(row=4, column=0, padx=20)

                            # creating a frame when no result is found
                            elif name == "" or name not in row_set:

                                disp_error = ttk.Frame(search_entry_window)
                                disp_error.grid(row=1, column=0, padx=20, pady=(0, 15))

                                disp_error = ttk.Label(disp_error, text="No result found")
                                disp_error.grid(row=0, column=0, padx=20, pady=10)

        # create new window when searching for an entry
            search_entry_window = Toplevel(self)
            search_entry_window.title("COVID Details Search Window")
            search_entry_window.configure(bg="#B2BEB5")

            # frame for the search entry
            search_widget = ttk.Frame(search_entry_window)
            search_widget.grid(row=0, column=0, padx=20, pady=15)

            # label for the search entry
            search_label = ttk.Label(search_widget, text="Search Last Name:")
            search_label.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

            # search entry box
            search_entry = ttk.Entry(search_widget)
            search_entry.grid(row=1, column=0, padx=10, pady=(0, 5))

            # button for the search entry
            search_btn = ttk.Button(search_widget, text="Search", command=search_entry_func)
            search_btn.grid(row=2, column=0, padx=10, pady=(0, 5))

            # exit button to exit search window
            exit_btn = ttk.Button(search_entry_window, text="Exit", command=exit_btn_func)
            exit_btn.grid(row=2, column=0, padx=20, pady=(0, 15))

    # create a frame inside a window
        widget = ttk.Frame(self)
        widget.grid(row=0, column=0, padx=(20, 0), pady=15)

    # personal information
        user_info = ttk.Labelframe(widget, text="Personal Information")
        user_info.grid(row=0, column=0, padx=(20), pady=10)

        # first name
        first_name_label = ttk.Label(user_info, text="First Name:")
        first_name_label.grid(row=0, column=0, padx=(20, 10), pady=5)

        first_name_entry = ttk.Entry(user_info)
        first_name_entry.grid(row=0, column=1, padx=(0, 20), pady=(0, 5))

        # last name
        last_name_label = ttk.Label(user_info, text="Last Name:")
        last_name_label.grid(row=1,column=0, padx=(20, 10), pady=(0, 10))

        last_name_entry = ttk.Entry(user_info)
        last_name_entry.grid(row=1,column=1, padx=(0, 20), pady=(0, 10))

    # COVID details
        covid_details = ttk.Labelframe(widget, text="COVID Details")
        covid_details.grid(row=1, column=0, padx=20, pady=(0, 10))

        # vaccination status
        vax_status_list = ["(Select Vaccination Status)", "Not Vaccinated", "Vaccinated - 1st Dose", "Vaccinated - 2nd Dose", 
                           "Vaccinated - 1st Booster", "Vaccinated - 2nd Booster"]
        self.vax_var = StringVar(self)

        vax_label = ttk.Label(covid_details, text="Please select your vaccination status:")
        vax_label.grid(row=0, column=0, padx=20, pady=(5, 0), sticky=EW)

        vax_opt = ttk.OptionMenu(covid_details, self.vax_var, *vax_status_list)
        vax_opt.configure(direction="below")
        vax_opt.grid(row=1, column=0, padx=20, pady=(0, 10), sticky=EW)

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

    # another widget to hold the 4 commands
        widget2 = ttk.Frame(self)
        widget2.grid(row=0, column=1,padx=(0, 20), pady=15)

        # clear button
        clear_btn = ttk.Button(widget2, text="Clear", command=clear_btn_func)
        clear_btn.grid(row=0, column=1, padx=(0, 20), pady=(143, 10))

        # add entry
        submit_btn = ttk.Button(widget2, text="Submit", command=add_entry)
        submit_btn.grid(row=1, column=1, padx=(0, 20), pady=(0, 10))

        # search entry
        search_btn = ttk.Button(widget2, text="Search", command=search_entry_window)
        search_btn.grid(row=2, column=1, padx=(0, 20), pady=(0, 10))

        # exit button
        exit_btn = ttk.Button(widget2, text="Exit", command=exit)
        exit_btn.grid(row=3, column=1, padx=(0, 20), pady=(0, 143))