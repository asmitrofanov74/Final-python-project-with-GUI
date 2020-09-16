import sqlite3
from tkinter.messagebox import _show


def submit(*get_data):
    conn = sqlite3.connect('pythonsqlite.db')
    c = conn.cursor()
    c.execute("""INSERT INTO  Users (User_name , Password , First_name , Last_name , Age , Address, City , Gender ) 
    VALUES(?,?,?,?,?,?,?,?);""",
              *get_data)
    conn.commit()
    conn.close()


def login(username, password):
    conn = sqlite3.connect('pythonsqlite.db')
    c = conn.cursor()
    sql = "SELECT * FROM Users WHERE User_name = ? and Password = ?"
    c.execute(sql, (username, password))
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result


def check_user(username):
    conn = sqlite3.connect('pythonsqlite.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Users WHERE User_name = ? ;", [username])
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result


def get_records(sql="select * from users where User_name = _rowid_"):
    conn = sqlite3.connect('pythonsqlite.db')
    records = conn.cursor().execute(sql).fetchall()
    conn.commit()
    conn.close()
    if len(records) == 0:
        _show('Message', 'No data in records!')
    return records


def confirm(*get_data):
    conn = sqlite3.connect('pythonsqlite.db')
    c = conn.cursor()
    c.execute("""INSERT INTO  Appointments (User_ID ,  Appointment_date , Appointment_time , Doctor ) 
    VALUES(?,?,?,?);""",
              *get_data)
    conn.commit()
    conn.close()


def check_availability(date, time, doctor):
    conn = sqlite3.connect('pythonsqlite.db')
    c = conn.cursor()
    c.execute("SELECT Doctor  FROM Appointments WHERE Appointment_date = ? AND Appointment_time = ? "
              "AND Doctor =?  "
              , (date, time, doctor))
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result


def check_app(date, time, user_id):
    conn = sqlite3.connect('pythonsqlite.db')
    c = conn.cursor()
    c.execute("SELECT User_ID  FROM Appointments WHERE Appointment_date = ? AND Appointment_time = ? "
              "AND User_ID =?  "
              , (date, time, user_id))
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result
