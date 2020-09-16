from tkinter import *
from tkinter.ttk import Combobox
import Login_form
from tkcalendar import Calendar, DateEntry


def close_window():
    app_window.destroy()


def open_window():
    app_window.mainloop()


def clear():
    idLabel.delete(0, END)
    idLabel.configure(bg='white')
    username.configure(bg='white')
    username.delete(0, END)


def insert(record):
    idLabel.insert(0, record[0][0])
    username.insert(0, record[0][1])


def get_data():
    return (idLabel.get(), date.get(),
            time.get(), doctor.get())


def disable_entry():
    idLabel.config(state=DISABLED)
    username.config(state=DISABLED)


def enable_entry():
    idLabel.config(state=NORMAL)
    username.config(state=NORMAL)


app_window = Toplevel(Login_form.window)
app_window.title("Appointment form")

all_comboboxes = []

data_frame = Frame(master=app_window, relief=RAISED, borderwidth=1)
data_frame.grid(padx=5, pady=5)

idLabel = Label(master=data_frame, text="User ID:")
idLabel.grid(row=0, column=0)

idLabel = Entry(master=data_frame, width=40)
idLabel.grid(row=0, column=1)

nameLabel = Label(master=data_frame, text="User Name:")
nameLabel.grid(row=1, column=0)

username = Entry(master=data_frame, width=40)
username.grid(row=1, column=1)

dateLabel = Label(master=data_frame, text="Appointment date:")
dateLabel.grid(row=2, column=0)

date = DateEntry(master=data_frame, width=37, background='darkblue',
                 foreground='white', borderwidth=2, year=2020)
date.grid(row=2, column=1)

timeLabel = Label(master=data_frame, text="Appointment time:")
timeLabel.grid(row=3, column=0)

time = Combobox(master=data_frame, width=37, values=("10:00", "10:15", "10:30", "10:45", "11:00", "11:15", "11:30"
                                                     , "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15"
                                                     , "13:30", "13:45", "14:00", "14:15", "14:30", "14:45"))
time.set("10:00")
time.grid(row=3, column=1)

docLabel = Label(master=data_frame, text="Doctor:")
docLabel.grid(row=4, column=0)

doctor = Combobox(master=data_frame, width=37, values=("Dr. Andy", "Dr. Charlie"))
doctor.set("Dr. Andy")
doctor.grid(row=4, column=1)

button_frame = Frame(master=app_window, relief=RAISED, borderwidth=1)
button_frame.grid(padx=5, pady=5)
checkAvBtn = Button(master=button_frame, text="Check availability", width=20)
checkAvBtn.grid(row=0, column=0)
conAvtBtn = Button(master=button_frame, text="Confirm appointment", width=20)
conAvtBtn.grid(row=0, column=1)
cancelBtn = Button(master=button_frame, text="Cancel", width=10)
cancelBtn.grid(row=0, column=2)

app_window.withdraw()
