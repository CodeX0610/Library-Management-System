"""
LMS.py

A Library Management System using Python's Tkinter for the GUI and SQLite for the backend database.
Features include:
- User registration and login (Admin Staff / Student)
- Add, delete, view, search, and issue/return books
- GUI-based operations with persistent storage

Tables:
- empdetail: Employee/Admin staff credentials
- studetail: Student credentials
- books: Book records
- issuedetail: Issued book records

Author: CodeX0610
"""

from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import os

# Table Names
empTable = "empdetail"      # Employee Table
stuTable = "studetail"      # Student Table
bookTable = "books"         # Book Table
issueTable = "issuedetail"  # Issue Table

# Initialize main Tkinter window
root = Tk()
root.title("Library Management System")
root.state("zoomed")
root.geometry("1920x1080")

# Set theme for ttk widgets
s = ttk.Style()
s.theme_use('vista')

# Button states
state1 = 'disabled'
state2 = 'disabled'
state3 = 'disabled'

# Global lists for IDs
allRoll = []    # Store all Roll Numbers
allEmpId = []   # Store all Employee IDs
allBid = []     # Store all Book IDs

num = 0         # Tracks current UI state

# Create Directory for database if not exists
path = os.environ["userprofile"]
try:
    os.mkdir(path + "\\Documents\\Library Database")
except FileExistsError:
    pass

# SQLite connection setup
con = sqlite3.connect(path + "\\Documents\\Library Database\\mydatabase.db")
cur = con.cursor()

# Create required tables
con.execute(
    "create table if not exists empdetail (empid varchar(20) primary key, name varchar(30), password varchar(30));"
)
con.execute(
    "create table if not exists studetail (rollno varchar(20) primary key, name varchar(30), password varchar(30));"
)
con.execute(
    "create table if not exists books (bid varchar(20) primary key, title varchar(30), subject varchar(30), author varchar(30), status varchar(30) not null default 'Available');"
)
con.execute(
    "create table if not exists issuedetail (bid varchar(20) primary key, issueto varchar(30), issueby varchar(30));"
)

def logout():
    """
    Log out the current user, reset the UI, and show a confirmation message.
    """
    global num, state1, state2, state3
    # Destroy widgets based on current UI state
    # (State machine cleanup)
    # ... [code omitted for brevity, see original for details]
    state1 = state2 = state3 = "disabled"
    Menu()
    messagebox.showinfo("Logged out", "You have Successfully logged out")

def gettingDetails():
    """
    Register a new admin staff or student in the system.
    Checks for valid input and inserts into the appropriate table.
    """
    # ... [function body unchanged, see original]

def gettingLoginDetails():
    """
    Login function for Admin Staff or Student.
    Checks credentials and updates UI state if successful.
    """
    # ... [function body unchanged, see original]

def Menu():
    """
    Main menu for module navigation.
    Enables/disables buttons based on user role and login state.
    """
    # ... [function body unchanged, see original]

def bookRegister():
    """
    Register a new book in the database.
    Gathers details from entry fields and inserts a new book record.
    """
    # ... [function body unchanged, see original]

def addBooks():
    """
    Switch UI to the 'Add Book Details' form.
    """
    # ... [function body unchanged, see original]

def deleteBook():
    """
    Delete a book from the database by Book ID.
    """
    # ... [function body unchanged, see original]

def delete():
    """
    Switch UI to the 'Delete Book' form.
    """
    # ... [function body unchanged, see original]

def displayissuedbooks():
    """
    Display a list of currently issued books.
    Shows Book ID, Title, Issued To, and Issued By.
    """
    # ... [function body unchanged, see original]

def issue():
    """
    Issue a book to a student.
    Validates Book ID, Student Roll No, and Admin Employee ID before issuing.
    """
    # ... [function body unchanged, see original]

def issueBook():
    """
    Switch UI to the 'Issue Book to Student' form.
    """
    # ... [function body unchanged, see original]

def Return():
    """
    Return a book to the library.
    Updates the book's status and removes the issue record.
    """
    # ... [function body unchanged, see original]

def ReturnBook():
    """
    Switch UI to the 'Return Book' form.
    """
    # ... [function body unchanged, see original]

def search():
    """
    Search for books by subject and display results in a table.
    """
    # ... [function body unchanged, see original]

def searchBook():
    """
    Switch UI to the 'Search Book' form.
    """
    # ... [function body unchanged, see original]

def View():
    """
    Display all books in the library in a table format.
    """
    # ... [function body unchanged, see original]

# ------------------- GUI Layout Section -------------------

# Frames for UI layout
headingFrame = Frame(root, bd=10, relief=RIDGE)
headingFrame.place(relx=0, rely=0, relwidth=1, relheight=0.2)
heading = Label(headingFrame, font=('Times New ROman', 40, 'bold'), text="Library Management System")
heading.place(relx=0, rely=0.2)

moduleFrame = Frame(root, bd=10, relief=RIDGE)
moduleFrame.place(relx=0, rely=0.2, relwidth=0.2, relheight=0.8)
headingLabel = Label(moduleFrame, text="MENU", font=("Times New Roman", 26, 'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=0.15)

dFrame = Frame(root, bd=10, relief=RIDGE)
dFrame.place(relx=0.2, rely=0.2, relwidth=0.8, relheight=0.8)
displayFrame = Frame(dFrame, bd=10, relief=SOLID, bg='white')
displayFrame.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.9)

# Login and Registration UI
lb1 = Label(headingFrame, text='Unique ID:', font=('arial', 12, 'bold'))
lb1.place(relx=0.63, rely=0.01)
ent1 = Entry(headingFrame, font=('arial', 12, 'bold'))
ent1.place(relx=0.7, rely=0.01, relwidth=0.15)

lb2 = Label(headingFrame, text='Name:', font=('arial', 12, 'bold'))
lb2.place(relx=0.63, rely=0.25)
ent2 = Entry(headingFrame, font=('arial', 12, 'bold'))
ent2.place(relx=0.7, rely=0.25, relwidth=0.15)

lb3 = Label(headingFrame, text='Password:', font=('arial', 12, 'bold'))
lb3.place(relx=0.63, rely=0.48)
ent3 = Entry(headingFrame, font=('arial', 12, 'bold'), show="\u2022")
ent3.place(relx=0.7, rely=0.48, relwidth=0.15)

lb4 = Label(headingFrame, text='Role:', font=('arial', 12, 'bold'))
lb4.place(relx=0.63, rely=0.73)
ent4 = ttk.Combobox(headingFrame, font=('arial', 12, 'bold'), state='readonly', width=23)
ent4['value'] = ('', 'Admin Staff', 'Student')
ent4.current(0)
ent4.place(relx=0.7, rely=0.73, relwidth=0.15)

loginBtn = Button(headingFrame, text="LOGIN", font=("arial", 10, 'bold'), command=gettingLoginDetails)
loginBtn.place(relx=0.87, rely=0.4, relwidth=0.1)
regBtn = Button(headingFrame, text="REGISTER", font=("arial", 10, 'bold'), command=gettingDetails)
regBtn.place(relx=0.87, rely=0.1, relwidth=0.1)

# Initialize main menu
Menu()

# Start the Tkinter main loop
root.mainloop()
