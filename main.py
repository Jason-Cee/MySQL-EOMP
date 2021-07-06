# JASON CALVERT MYSQL END OF MODULE PROJECT

from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox

# IMPORTS
import mysql.connector

# CONNECTING TO DATABASE
mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                               database='LifeChoices_Online')

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
log = Label(frame_left, text="LOGIN", font=("Ariel", 20), bg="#346ab3", fg="#9ccb3b")
log.place(x=150, y=10)
# NAME & SURNAME LABEL AND ENTRY
user = Label(frame_left, text="Name & Surname:", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b")
user.place(x=10, y=100)
user_ent = Entry(frame_left, bg="#9ccb3b", fg="black")
user_ent.place(x=200, y=101)

# PASSWORD LABEL AND ENTRY
passw = Label(frame_left, text="Class (1 / 2):", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b")
passw.place(x=10, y=200)
passw_ent = Entry(frame_left, bg="#9ccb3b", fg="black")
passw_ent.place(x=200, y=200)


# SIGN IN BUTTON AND FUNCTIONALITY

def here():
    if user_ent == "":
        messagebox.showerror("INVALID", "PLEASE ENTER NAME AND SURNAME")
        user_ent.delete(0, END)
        passw_ent.delete(0, END)

    elif passw_ent == "":
        messagebox.showerror("INVALID", "PLEASE ENTER VALID CLASS")
    else:
        messagebox.showinfo("YOU ARE IN", "HAVE AN AMAZING DAY.")
        root.destroy()
        import out


sign = Button(frame_left, text="SIGN IN", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3", command=here)
sign.place(x=150, y=350)


# GIVING CLEAR BUTTON FUNCTIONALITY
def clear():
    user_ent.delete(0, END)
    passw_ent.delete(0, END)


# CLEAR BUTTON
remove = Button(frame_left, text="CLEAR", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3", command=clear)
remove.place(x=155, y=290)

# GREEN FRAME
frame_right = Frame(root, width=400, height=400, bg="#9ccb3b")
frame_right.place(x=500, y=200)
reg = Label(frame_right, text="REGISTER", font=("Ariel", 20), bg="#9ccb3b", fg="#346ab3")
reg.place(x=130, y=10)

# LABEL
label1 = Label(frame_right, text="DETAILS NOT IN OUR" + "\n" "SYSTEM ?", font=("Ariel", 20), bg="#9ccb3b", fg="#346ab3")
label1.place(x=60, y=110)
label2 = Label(frame_right, text="REGISTER NOW", font=("Ariel", 20), bg="#9ccb3b", fg="#346ab3")
label2.place(x=100, y=240)


# SIGN UP BUTTON AND FUNCTIONALITY
def inn():
    msg = messagebox.showinfo("REGISTER NOW", "YOU ARE GOING TO REGISTER WINDOW")
    if msg == "ok":
        root.destroy()
        import register


sign_in = Button(frame_right, text="REGISTER", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b", command=inn)
sign_in.place(x=145, y=320)


# EXIT BUTTON AND FUNCTIONALITY
def outt():
    msg = messagebox.askquestion("GONE SO SOON", " ARE YOU SURE YOU WANT TO EXIT ?")
    if msg == "yes":
        root.destroy()


destroy = Button(root, text="E X I T", font=("Ariel", 13), bg="black", fg="#f7f7f7", command=outt)
destroy.place(x=455, y=700)

root.mainloop()
