from tkinter import *
import Login_form


def validate():
    didPass = True

    if username.get() == "":
        username.configure(bg='#FF8786')
        username.insert(0, "You must enter your username")
        didPass = False
    if password.get() == "":
        password.configure(bg='#FF8786')
        password.insert(0, "You must enter your password")
        didPass = False
    if fname.get() == "":
        fname.configure(bg='#FF8786')
        fname.insert(0, "You must enter your first name")
        didPass = False
    if lname.get() == "":
        lname.configure(bg='#FF8786')
        lname.insert(0, "You must enter your last name")
        didPass = False
    if age.get() == "":
        age.configure(bg='#FF8786')
        age.insert(0, "You must enter your age")
        didPass = False
    if city.get() == "":
        city.configure(bg='#FF8786')
        city.insert(0, "You must enter your city")
        didPass = False
    if address.get() == "":
        address.configure(bg='#FF8786')
        address.insert(0, "You must enter your address")
        didPass = False

    return didPass


def clear():
    username.configure(bg='white')
    username.delete(0, END)
    password.configure(bg='white')
    password.delete(0, END)
    fname.configure(bg='white')
    fname.delete(0, END)
    lname.configure(bg='white')
    lname.delete(0, END)
    age.configure(bg='white')
    age.delete(0, END)
    address.configure(bg='white')
    address.delete(0, END)
    city.configure(bg='white')
    city.delete(0, END)
    gender.set('Male')


def insert(records, index):
    clear()
    username.insert(0, records[index][0])
    password.insert(0, records[index][1])
    fname.insert(0, records[index][2])
    lname.insert(0, records[index][3])
    gender.set(records[index][7])


def close_window():
    reg_window.destroy()


def open_window():
    reg_window.mainloop()


def get_data():
    return (username.get(), password.get(), fname.get(),
            lname.get(), age.get(), address.get(),
            city.get(), gender.get())


reg_window = Toplevel(Login_form.window)
reg_window.title("Registration form")

data_frame = Frame(master=reg_window, relief=RAISED, borderwidth=1)
data_frame.grid(padx=5, pady=5)


usernameLabel = Label(master=data_frame, text="Username:")
usernameLabel.grid(row=0, column=0)

username = Entry(master=data_frame, width=50)
username.grid(row=0, column=1)

passwordLabel = Label(master=data_frame, text="Password:")
passwordLabel.grid(row=1, column=0)

password = Entry(master=data_frame, width=50, show='*')
password.grid(row=1, column=1)

fnameLabel = Label(master=data_frame, text="First name:")
fnameLabel.grid(row=2, column=0)

fname = Entry(master=data_frame, width=50)
fname.grid(row=2, column=1)

lnameLabel = Label(master=data_frame, text="Last name:")
lnameLabel.grid(row=3, column=0)

lname = Entry(master=data_frame, width=50)
lname.grid(row=3, column=1)

addressLabel = Label(master=data_frame, text="Address:")
addressLabel.grid(row=5, column=0)

address = Entry(master=data_frame, width=50)
address.grid(row=5, column=1)

ageLabel = Label(master=data_frame, text="Age:")
ageLabel.grid(row=4, column=0)

age = Entry(master=data_frame, width=50)
age.grid(row=4, column=1)

cityLabel = Label(master=data_frame, text="City:")
cityLabel.grid(row=6, column=0)

city = Entry(master=data_frame, width=50)
city.grid(row=6, column=1)

availability_frame = Frame(master=reg_window, relief=RAISED, borderwidth=1)
availability_frame.grid(padx=5, pady=5)

genderLabel = Label(master=availability_frame, text="Gender:")
genderLabel.grid(row=0, column=0)

gender = StringVar()
gender.set("Male")
rad1 = Radiobutton(master=availability_frame, text='Male', value="Male", variable=gender)
rad1.grid(row=0, column=1, sticky=W)
rad2 = Radiobutton(master=availability_frame, text='Female', value="Female", variable=gender)
rad2.grid(row=0, column=2, sticky=W)
rad3 = Radiobutton(master=availability_frame, text='Other', value="Other", variable=gender)
rad3.grid(row=0, column=3, sticky=W)

button_frame = Frame(master=reg_window, relief=RAISED, borderwidth=1)
button_frame.grid(padx=5, pady=5)
submitBtn = Button(master=button_frame, text="Submit", width=10)
submitBtn.grid(row=0, column=0)
cancelBtn = Button(master=button_frame, text="Cancel", width=10)
cancelBtn.grid(row=0, column=1)


reg_window.withdraw()

