# JASON CALVERT MYSQL END OF MODULE PROJECT

from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
from datetime import *

# IMPORTS
import mysql.connector

# WINDOW
root = Tk()
root.title("Lifechoices Online")  # WINDOW TITLE
root.geometry("1000x800")  # WINDOW SIZE
root.resizable(False, False)  # CAN'T CHANGE SIZE MANUALLY
# root.config(bg="white")  # WINDOW COLOR

now = datetime.now()

# LIFECHOICES IMAGE / LOGO
img = PhotoImage(file="lca1.png")
Label(root, image=img).place(x=290, y=10)  # IMAGE / LOGO PLACEMENT

# BLUE FRAME
frame_left = Frame(root, width=400, height=400, bg="#346ab3")
frame_left.place(x=100, y=200)
log = Label(frame_left, text="STUDENT LOGIN", font=("Ariel", 20), bg="#346ab3", fg="#9ccb3b")
log.place(x=85, y=10)
# NAME & SURNAME LABEL AND ENTRY
user = Label(frame_left, text="Name & Surname:", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b")
user.place(x=10, y=100)
user_ent = Entry(frame_left, bg="#9ccb3b", fg="black")
user_ent.place(x=200, y=101)

# PASSWORD LABEL AND ENTRY
passid = Label(frame_left, text="ID Number:", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b")
passid.place(x=10, y=200)
passid_ent = Entry(frame_left, bg="#9ccb3b", fg="black")
passid_ent.place(x=200, y=200)
def go():
if user_ent.get() == "" and phone_ent.get() == "" and email_ent.get() == "" and id_num_ent.get() == "":
    messagebox.showerror("INVALID", "PLEASE ENTER YOUR DETAILS")
else:
    mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
                                   database="LifeChoices_Online", auth_plugin="mysql_native_password")
    mycursor = mydb.cursor()

    sql = "INSERT INTO User (Name, Id_Number) VALUES (%s, %s)"
    val = (user_ent.get(), phone_ent.get(), email_ent.get(), id_num_ent.get())
    mycursor.execute(sql, val)

    mydb.commit()
    print(mycursor.rowcount, "Details Recorded.")
    mycursor.execute("Select * from User")

sign = Button(frame_left, text="SIGN IN", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3", command=go)
sign.place(x=255, y=350)


# GIVING CLEAR BUTTON FUNCTIONALITY
def clear():
    user_ent.delete(0, END)
    passid_ent.delete(0, END)


# CLEAR BUTTON
remove = Button(frame_left, text="CLEAR", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3", command=clear)
remove.place(x=50, y=300)

# GREEN FRAME
frame_right = Frame(root, width=400, height=400, bg="#9ccb3b")
frame_right.place(x=500, y=200)
admin = Label(frame_right, text="ADMIN STAFF", font=("Ariel", 20), bg="#9ccb3b", fg="#346ab3")
admin.place(x=110, y=10)

# LABEL
label1 = Label(frame_right, text="Username:", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3")
label1.place(x=10, y=100)
label1_ent = Entry(frame_right, bg="#346ab3", fg="black")
label1_ent.place(x=210, y=100)

# NAME & SURNAME LABEL AND ENTRY
label2 = Label(frame_right, text="Password:", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3")
label2.place(x=10, y=200)
label2_ent = Entry(frame_right, bg="#346ab3", fg="black")
label2_ent.place(x=210, y=200)

sign_in = Button(frame_right, text="SIGN IN", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b")
sign_in.place(x=50, y=350)

cleans = Button(frame_right, text="CLEAR", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b")
cleans.place(x=260, y=300)


# EXIT BUTTON AND FUNCTIONALITY
def outt():
    msg = messagebox.askquestion("GONE SO SOON", " ARE YOU SURE YOU WANT TO EXIT ?")
    if msg == "yes":
        root.destroy()


destroy = Button(root, text="E X I T", font=("Ariel", 13), bg="black", fg="#f7f7f7", command=outt)
destroy.place(x=455, y=700)


# REGISTER LABEL AND BUTTON FUNCTIONALITY
def inn():
    msg = messagebox.showinfo("REGISTER NOW", "YOU ARE GOING TO REGISTER WINDOW")
    if msg == "ok":
        root.destroy()
        import register


reg = Label(root, text="Details not in our system?", font=("Ariel", 10), fg="black")
reg.place(x=350, y=760)
regbtn = Button(root, text="Register Here", borderwidth=0, font=("Ariel", 10), fg="black", command=inn)
regbtn.place(x=530, y=756)

root.mainloop()
