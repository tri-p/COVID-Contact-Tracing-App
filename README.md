# COVID-Contact-Tracing-App

## About the project
The COVID Contact Tracing App is an application written in Python that allows the user to input their personal information and COVID details. The program allows the user to search for an entry with the surname of the person they are looking for, and the details they entered will appear on the window. The program uses the GUI Tkinter to make the application. OOP was also implemented in this project to easily modify the files simultaneously.

### Files in making the app
- application.py
  > Contains all the code for the application.

- details.csv
  > The destination of the details entered by the user. Stores data for the application to read.

- main_app.py
  > Starts the main event loop for the program which will display the application and will allow interaction with the user.

### To run the program
1. Install Python on your computer to run the code. You can download it here: https://www.python.org/downloads/
2. Open the software and make three separate files just like in the repository. Paste the code from the three files.
3. Save the files with a .py extension and a .csv extension for the CSV file.
4. You can delete the list on your CSV file. Make sure that it is comma-separated and it matches the columns
5. Run the file main_app.py. A GUI will appear.
6. You may input your personal information on the entry boxes and enter the COVID-related questions that are asked.
7. On the right side of the GUI, there are four commands you can do: Clear, Submit, Search, Exit
8. The 'Clear' button clears the entire form.
9. The 'Submit' button adds the entered data to the CSV file.
10. The 'Search' button takes the user to another window that will prompt the user to enter the last name of the person they are looking for. The search entry box is strictly for last names.
11. If the person is on the CSV file, their details will pop on the window. Otherwise, the window will display 'No result found'.
12. The 'Exit' button is to exit the window or end the program.

### Demo
You can access my demo through this link: 
https://drive.google.com/file/d/1arrrakJqDRFSHuXbicYEnz2z0G34f57V/view?usp=drive_link
