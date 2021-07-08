# IMPORTS
import mysql.connector
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox

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
phone.place(x=10, y=140)
phone_ent = Entry(frame_left, bg="#9ccb3b", fg="black")
phone_ent.place(x=210, y=140)

# EMAIL ADDRESS LABEL AND ENTRY
email = Label(frame_left, text="Email Address:", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b")
email.place(x=10, y=200)
email_ent = Entry(frame_left, bg="#9ccb3b", fg="black")
email_ent.place(x=210, y=200)

# ID NUMBER LABEL AND ENTRY
id_num = Label(frame_left, text="ID Number:", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b")
id_num.place(x=10, y=260)
id_num_ent = Entry(frame_left, bg="#9ccb3b", fg="black")
id_num_ent.place(x=210, y=260)


# CLEAR BUTTON AND FUNCTIONALITY
def wipe():
    user_ent.delete(0, END)
    phone_ent.delete(0, END)
    email_ent.delete(0, END)
    id_num_ent.delete(0, END)


clean = Button(frame_left, text="CLEAR", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3", command=wipe)
clean.place(x=50, y=300)


# SUBMIT BUTTON AND FUNCTIONALITY
def submit():
    if user_ent.get() == "" and phone_ent.get() == "" and email_ent.get() == "" and id_num_ent.get() == "":
        messagebox.showerror("INVALID", "PLEASE ENTER YOUR DETAILS")
    else:
        mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
                                       database="LifeChoices_Online", auth_plugin="mysql_native_password")
        mycursor = mydb.cursor()

        sql = "INSERT INTO User (Name, Mobile_Number, Email_Address, Id_Number) VALUES (%s, %s, %s, %s)"
        val = (user_ent.get(), phone_ent.get(), email_ent.get(), id_num_ent.get())
        mycursor.execute(sql, val)

        mydb.commit()
        print(mycursor.rowcount, "Details Recorded.")
        mycursor.execute("Select * from User")
        messagebox.showinfo("SUCCESS", "PLEASE ADD NEXT OF KIN DETAILS AS WELL")

        users_ent["state"] = "normal"
        phones_ent["state"] = "normal"


enter = Button(frame_left, text="SUBMIT", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3", command=submit)
enter.place(x=255, y=350)

# GREEN FRAME
frame_right = Frame(root, width=400, height=400, bg="#9ccb3b")
frame_right.place(x=500, y=200)
reg = Label(frame_right, text="NEXT OF KIN DETAILS", font=("Ariel", 20), bg="#9ccb3b", fg="#346ab3")
reg.place(x=50, y=10)

# NAME & SURNAME LABEL AND ENTRY
users = Label(frame_right, text="Name & Surname:", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3")
users.place(x=10, y=100)
users_ent = Entry(frame_right, bg="#346ab3", fg="black", state="disabled")
users_ent.place(x=210, y=100)

# MOBILE NUMBER LABEL AND ENTRY
phones = Label(frame_right, text="Mobile Number:", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3")
phones.place(x=10, y=210)
phones_ent = Entry(frame_right, bg="#346ab3", fg="black", state="disabled")
phones_ent.place(x=210, y=210)


# SUBMIT BUTTON AND FUNCTIONALITY
def submit():
    if user_ent.get() == "" and phone_ent.get() == "" and email_ent.get() == "" and id_num_ent.get() == "":
        messagebox.showerror("INVALID", "PLEASE ENTER YOUR DETAILS")
    else:
        mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
                                       database="LifeChoices_Online", auth_plugin="mysql_native_password")
        mycursor = mydb.cursor()

        sql = "INSERT INTO Next_Of_Kin (Name, Mobile_Number, User_Id) VALUES (%s, %s, '13')"
        val = (users_ent.get(), phones_ent.get())
        mycursor.execute(sql, val)

        mydb.commit()
        print(mycursor.rowcount, "Details Recorded.")
        mycursor.execute("Select * from Next_Of_Kin")
        messagebox.showinfo("SUCCESS", "DETAILS RECORDED")
        import main


enters = Button(frame_right, text="SUBMIT", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b", command=submit)
enters.place(x=50, y=350)


# CLEAR BUTTON AND FUNCTIONALITY
def wipes():
    users_ent.delete(0, END)
    phones_ent.delete(0, END)


cleans = Button(frame_right, text="CLEAR", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b", command=wipes)
cleans.place(x=260, y=300)


# EXIT BUTTON AND FUNCTIONALITY
def out():
    msg = messagebox.askquestion("GONE SO SOON", " ARE YOU SURE YOU WANT TO EXIT ?")
    if msg == "yes":
        root.destroy()


destroy = Button(root, text="E X I T", font=("Ariel", 13), bg="black", fg="#f7f7f7", command=out)
destroy.place(x=455, y=700)

# RUN CODE
root.mainloop()
