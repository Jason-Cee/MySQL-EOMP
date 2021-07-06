# IMPORTS
import mysql.connector
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox

# CONNECTING TO DATABASE
mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                               database='LifeChoices_Online', auth_plugin='mysql_native_password')

mycursor = mydb.cursor()

# WINDOW
root = Tk()
root.title("Lifechoices Online")  # WINDOW TITLE
root.geometry("1000x800")  # WINDOW SIZE
root.resizable(False, False)  # CAN'T CHANGE SIZE MANUALLY
# root.config(bg="white")  # WINDOW COLOR

# LIFECHOICES IMAGE / LOGO
img = PhotoImage(file="lca1.png")
Label(root, image=img).place(x=290, y=10)  # IMAGE / LOGO PLACEMENT

# BLUE FRAME
frame_left = Frame(root, width=400, height=400, bg="#346ab3")
frame_left.place(x=100, y=200)
log = Label(frame_left, text="YOUR DETAILS", font=("Ariel", 20), bg="#346ab3", fg="#9ccb3b")
log.place(x=100, y=10)

# NAME & SURNAME LABEL AND ENTRY
user = Label(frame_left, text="Name & Surname:", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b")
user.place(x=10, y=80)
user_ent = Entry(frame_left, bg="#9ccb3b", fg="black")
user_ent.place(x=210, y=80)

# MOBILE NUMBER LABEL AND ENTRY
phone = Label(frame_left, text="Mobile Number:", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b")
phone.place(x=10, y=120)
phone_ent = Entry(frame_left, bg="#9ccb3b", fg="black")
phone_ent.place(x=210, y=120)

# EMAIL ADDRESS LABEL AND ENTRY
email = Label(frame_left, text="Email Address:", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b")
email.place(x=10, y=160)
email_ent = Entry(frame_left, bg="#9ccb3b", fg="black")
email_ent.place(x=210, y=160)

# ID NUMBER LABEL AND ENTRY
id_num = Label(frame_left, text="ID Number:", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b")
id_num.place(x=10, y=200)
id_num_ent = Entry(frame_left, bg="#9ccb3b", fg="black")
id_num_ent.place(x=210, y=200)

# PASSWORD LABEL AND ENTRY
password = Label(frame_left, text="Password:", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b")
password.place(x=10, y=240)
password_ent = Entry(frame_left, bg="#9ccb3b", fg="black")
password_ent.place(x=210, y=240)

# CLEAR BUTTON AND FUNCTIONALITY
def wipe():
    user_ent.delete(0, END)
    phone_ent.delete(0, END)
    email_ent.delete(0, END)
    id_num_ent.delete(0, END)
    password_ent.delete(0, END)


clean = Button(frame_left, text="CLEAR", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3", command=wipe)
clean.place(x=50, y=300)


# SUBMIT BUTTON AND FUNCTIONALITY
# def submit():
#
#
enter = Button(frame_left, text="SUBMIT", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3")
enter.place(x=255, y=350)

# GREEN FRAME
frame_right = Frame(root, width=400, height=400, bg="#9ccb3b")
frame_right.place(x=500, y=200)
reg = Label(frame_right, text="NEXT OF KIN DETAILS", font=("Ariel", 20), bg="#9ccb3b", fg="#346ab3")
reg.place(x=50, y=10)

# NAME & SURNAME LABEL AND ENTRY
users = Label(frame_right, text="Name & Surname:", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3")
users.place(x=10, y=80)
users_ent = Entry(frame_right, bg="#346ab3", fg="black")
users_ent.place(x=210, y=80)

# MOBILE NUMBER LABEL AND ENTRY
phones = Label(frame_right, text="Mobile Number:", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3")
phones.place(x=10, y=130)
phones_ent = Entry(frame_right, bg="#346ab3", fg="black")
phones_ent.place(x=210, y=130)

# EMAIL ADDRESS LABEL AND ENTRY
emails = Label(frame_right, text="Email Address:", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3")
emails.place(x=10, y=180)
emails_ent = Entry(frame_right, bg="#346ab3", fg="black")
emails_ent.place(x=210, y=180)

# ID NUMBER LABEL AND ENTRY
id_nums = Label(frame_right, text="ID Number:", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3")
id_nums.place(x=10, y=230)
id_nums_ent = Entry(frame_right, bg="#346ab3", fg="black")
id_nums_ent.place(x=210, y=230)


# SUBMIT BUTTON AND FUNCTIONALITY
# def submit():
#
#
enters = Button(frame_right, text="SUBMIT", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b")
enters.place(x=50, y=350)


# CLEAR BUTTON AND FUNCTIONALITY
def wipes():
    users_ent.delete(0, END)
    phones_ent.delete(0, END)
    emails_ent.delete(0, END)
    id_nums_ent.delete(0, END)


cleans = Button(frame_right, text="CLEAR", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b", command=wipes)
cleans.place(x=260, y=300)


root.mainloop()
