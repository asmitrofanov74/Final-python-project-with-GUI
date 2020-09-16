from tkinter.messagebox import _show

import Login_form
import Database
import Registration_form
import Appointment_form


def register_clicked(event):
    Login_form.login_window.withdraw()
    Registration_form.reg_window.deiconify()


def quit_clicked(event):
    Login_form.login_window.quit()


def login_clicked(event):
    if Login_form.validate():
        result = Database.login(Login_form.username.get(), Login_form.password.get())
        if result:
            Login_form.login_window.withdraw()
            Appointment_form.app_window.deiconify()
            record = Database.check_user(Login_form.username.get())
            Appointment_form.enable_entry()
            Appointment_form.insert(record)
            Appointment_form.disable_entry()
            Login_form.clear()
        else:
            _show('Message', 'User not exist or password and username incorrect!')
            Login_form.clear()


def submit_clicked(event):
    if Registration_form.validate():
        check_username = Database.check_user(Registration_form.username.get())
        if check_username:
            _show('Message', 'Username already use! try another username! ')
            Registration_form.clear()
        else:
            Appointment_form.enable_entry()
            Database.submit(Registration_form.get_data())
            record = Database.check_user(Registration_form.username.get())
            Registration_form.clear()
            Appointment_form.app_window.deiconify()
            Registration_form.reg_window.withdraw()
            Appointment_form.insert(record)
            Appointment_form.disable_entry()


def cancel_clicked(event):
    Registration_form.reg_window.withdraw()
    Login_form.login_window.deiconify()


def cancel2_clicked(event):
    Appointment_form.app_window.withdraw()
    Login_form.login_window.deiconify()
    Appointment_form.enable_entry()
    Appointment_form.clear()
    Appointment_form.disable_entry()


def check_availability_clicked(event):
    Appointment_form.enable_entry()
    check_availability = Database.check_availability(Appointment_form.date.get(), Appointment_form.time.get(),
                                                     Appointment_form.doctor.get())
    if check_availability:
        _show('Message', 'This time and date for this doctor already busy! try another time or date! ')
        Appointment_form.disable_entry()
    else:
        _show('Message', 'This time and date for this doctor free! You can make an appointment! ')
        Appointment_form.disable_entry()


def confirm_appointment_clicked(event):
    Appointment_form.enable_entry()
    check_appointment = Database.check_app(Appointment_form.date.get(), Appointment_form.time.get(),
                                           Appointment_form.idLabel.get())
    check_availability = Database.check_availability(Appointment_form.date.get(), Appointment_form.time.get(),
                                                     Appointment_form.doctor.get())
    if check_appointment:
        _show('Message', 'You have appointment for this time and date! Try another time or date! ')
        Appointment_form.disable_entry()
    elif check_availability:
        _show('Message', 'This time and date for this doctor already busy! try another time or date! ')
        Appointment_form.disable_entry()

    else:
        Database.confirm(Appointment_form.get_data())
        _show('Message', 'You have made an appointment! Thank you for using our application! ')
        Appointment_form.app_window.withdraw()
        Login_form.login_window.deiconify()
        Login_form.clear()
        Appointment_form.clear()
        Appointment_form.disable_entry()


Login_form.loginBtn.bind('<ButtonRelease-1>', login_clicked)
Login_form.registerBtn.bind('<Button-1>', register_clicked)
Login_form.quitBtn.bind('<Button-1>', quit_clicked)
Registration_form.submitBtn.bind('<ButtonRelease-1>', submit_clicked)
Registration_form.cancelBtn.bind('<Button-1>', cancel_clicked)
Appointment_form.checkAvBtn.bind('<ButtonRelease-1>', check_availability_clicked)
Appointment_form.conAvtBtn.bind('<ButtonRelease-1>', confirm_appointment_clicked)
Appointment_form.cancelBtn.bind('<Button-1>', cancel2_clicked)
Login_form.login_window.mainloop()
