# IMPORTS
import mysql.connector
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox

# CONNECTING TO DATABASE
mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                               database='Lifechoices_Online')

mycursor = mydb.cursor()

# WINDOW
root = Tk()
root.title("Lifechoices Online")  # WINDOW TITLE
root.geometry("1000x800")  # WINDOW SIZE
root.resizable(False, False)  # CAN'T CHANGE SIZE MANUALLY
# root.config(bg="white")  # WINDOW COLOR

# LIFECHOICES IMAGE / LOGO
img = PhotoImage(file="lca.png")
Label(root, image=img).place(x=150, y=0)  # IMAGE / LOGO PLACEMENT

# BLUE FRAME
frame_left = Frame(root, width=400, height=400, bg="#346ab3")
frame_left.place(x=100, y=300)
log = Label(frame_left, text="ALL ABOUT YOU", font=("Ariel", 20), bg="#346ab3", fg="#9ccb3b")
log.place(x=90, y=10)

rate = Label(frame_left, text="PLEASE RATE YOUR DAY", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b")
rate.place(x=85, y=90)
check = Spinbox(frame_left, from_=1, to_=10, width=2, font=("Ariel", 30), bg="#9ccb3b", fg="#346ab3")
check.place(x=150, y=175)

# SUBMIT BUTTON AND FUNCTIONALITY
def submit():
    messagebox.showinfo("THANK YOU")


enter = Button(frame_left, text="SUBMIT", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3", command=submit)
enter.place(x=255, y=350)


# CLEAR BUTTON AND FUNCTIONALITY
def wipe():
    check.delete(0, END)


clean = Button(frame_left, text="CLEAR", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3", command=wipe)
clean.place(x=50, y=300)

# GREEN FRAME
frame_right = Frame(root, width=400, height=400, bg="#9ccb3b")
frame_right.place(x=500, y=300)
reg = Label(frame_right, text="SIGN OUT", font=("Ariel", 20), bg="#9ccb3b", fg="#346ab3")
reg.place(x=130, y=10)


# SUBMIT BUTTON AND FUNCTIONALITY
# def submit():

def sign_out():
    messagebox.showinfo("SUCCESS", "SIGNED OUT, BE SAFE")
    root.destroy()


enters = Button(frame_right, text="SIGN OUT", font=("Ariel", 13), bg="#346ab3", fg="#9ccb3b", command=sign_out)
enters.place(x=140, y=350)


# EXIT BUTTON AND FUNCTIONALITY
def out():
    msg = messagebox.askquestion("GONE SO SOON", " ARE YOU SURE YOU WANT TO EXIT ?")
    if msg == "yes":
        root.destroy()


destroying = Button(root, text="E X I T", font=("Ariel", 13), bg="black", fg="#f7f7f7", command=out)
destroying.place(x=455, y=735)


# RUN CODE
root.mainloop()
