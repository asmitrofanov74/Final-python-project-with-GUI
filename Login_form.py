from tkinter import *
from tkinter.messagebox import _show


def validate():
    didPass = True

    if username.get() == "":
        username.configure(bg='#FF8786')
        username.insert(0, "You must enter your username")
        _show('Message', 'You have to enter your username!')
        didPass = False
    if password.get() == "":
        password.configure(bg='#FF8786')
        password.insert(0, "Must enter your address")
        _show('Message', 'You have to enter your password!')
        didPass = False

    return didPass


def clear():
    username.configure(bg='white')
    username.delete(0, END)
    password.configure(bg='white')
    password.delete(0, END)


def close_window():
    login_window.destroy()


def open_window():
    login_window.mainloop()


def insert(records, index):
    clear()
    username.insert(0, records[index][0])
    password.insert(0, records[index][1])


def get_data():
    return username.get(), password.get()


window = Tk()
login_window = Toplevel(window)
login_window.title("Login form")

data_frame = Frame(master=login_window, relief=RAISED, borderwidth=1)
data_frame.grid(padx=5, pady=5)

usernameLabel = Label(master=data_frame, text="Username:")
usernameLabel.grid(row=1, column=0)

username = Entry(master=data_frame, width=40)
username.grid(row=1, column=1)

passwordLabel = Label(master=data_frame, text="Password:")
passwordLabel.grid(row=2, column=0)

password = Entry(master=data_frame, width=40, show='*')
password.grid(row=2, column=1)

button_frame = Frame(master=login_window, relief=RAISED, borderwidth=1)
button_frame.grid(padx=5, pady=5)
loginBtn = Button(master=button_frame, text="Login", width=10)
loginBtn.grid(row=0, column=0)
registerBtn = Button(master=button_frame, text="Register", width=10)
registerBtn.grid(row=0, column=1)
quitBtn = Button(master=button_frame, text="Quit", width=10)
quitBtn.grid(row=0, column=2)

window.withdraw()
