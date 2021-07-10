# JASON CALVERT MYSQL END OF MODULE PROJECT
import datetime
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
from datetime import datetime

# IMPORTS
import mysql.connector

# WINDOW
root = Tk()
root.title("Lifechoices Online")  # WINDOW TITLE
root.geometry("1000x800")  # WINDOW SIZE
root.resizable(False, False)  # CAN'T CHANGE SIZE MANUALLY
# root.config(bg="white")  # WINDOW COLOR

# now = datetime.now()

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
    try:
        mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
                                       database="Lifechoices_Online", auth_plugin="mysql_native_password")

        mycursor = mydb.cursor()

        if user_ent.get() == "" or passid_ent.get() == "":
            messagebox.showerror("Error", "All Fields Are Required")
        else:
            mycursor.execute('select * from Login where Name=%s and Id_Number=%s',
                             (user_ent.get(), passid_ent.get()))

            row = mycursor.fetchone()
            if row is None:
                messagebox.showerror("USER DOES NOT EXIST", "PLEASE REGISTER DETAILS")
                msg = messagebox.askquestion("Plan A", "WOULD YOU LIKE TO GO TO REGISTER WINDOW ?")
                if msg == "yes":
                    root.destroy()
                    import register
            else:
                sql = "Insert into Login (Name, Time_in) values (%s, %s)"
                current_date = "curdate()"
                current_time = "curtime()"
                mycursor.execute(sql, current_date, current_time)
                mydb.commit()
                messagebox.showinfo(message="Login Successful! Enjoy Your Day!")
                root.destroy()
                import out

        # if row is None:
        #     messagebox.showerror("Error", "Invalid Name or ID")
        #     user_ent.delete(0, END)
        #     passid_ent.delete(0, END)
        #     user_ent.focus_set()
        # else:
        #     cursor.execute(
        #         "INSERT INTO Login (Time_in) values(curdate(), curtime())")
        #     db.commit()
        #     db.close()
        #     messagebox.showinfo("Successful Sign In", "Welcome " + user_ent.get())
        #     root.destroy()

    except ValueError:
        messagebox.showerror("OOPS", "INVALID NAME OR ID")
        user_ent.delete(0, END)
        passid_ent.delete(0, END)
        user_ent.focus()

    # try:
    #     mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
    #                                    database="Lifechoices_Online", auth_plugin="mysql_native_password")
    #
    #     mycursor = mydb.cursor()
    #
    #     # name = user_ent.get()
    #     id_number = passid_ent.get()
    #     query = "Select * from Login where Id_Number='{}'".format(id_number)
    #     mycursor.execute(query)
    #     result = mycursor.fetchall()
    #     if not result:
    #         messagebox.showerror("OOPS", "USER DOES NOT EXIT")
    #     else:
    #         # now = datetime.now()
    #         # today = "{}".format(now.date())
    #         # min = now.minute
    #         # hr = now.hour
    #         # if min <= 9:
    #         #     min = '0' + str(min)
    #         # if hr <= 9:
    #         #     hr = '0' + str(hr)
    #         # time = "{}:{}".format(hr, min)
    #         queryA = "Insert into Login (Time_in) values (curdate(), curtime())"
    #         mycursor.execute(queryA)
    #         mydb.commit()
    #         root.destroy()
    #         import out
    #
    # except ValueError:
    #     messagebox.showwarning("ERROR", "PLEASE TRY AGAIN")

    # if user_ent.get() == "" and user_ent.get() == "" and passid_ent.get() == "":
    #     messagebox.showerror("INVALID", "PLEASE ENTER YOUR DETAILS")
    # else:
    #     mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
    #                                    database="LifeChoices_Online", auth_plugin="mysql_native_password")
    #     mycursor = mydb.cursor()
    #
    #     sql = "UPDATE User SET Name = user_ent.get(), Id_Number = passid_ent.get()"
    #     val = (user_ent.get(), passid_ent.get())
    #     mycursor.execute(sql, val)
    #
    #     mydb.commit()
    #     print(mycursor.rowcount, "Details Recorded.")
    #     mycursor.execute("Select * from User")


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
