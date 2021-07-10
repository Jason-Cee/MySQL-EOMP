import mysql.connector
from tkinter import *
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Admin Users Page")
root.geometry("1054x800")
root.config()

# Background Image
bg_img = PhotoImage(file="lca.png")
bg_img = bg_img.subsample(5)
bg_img_lbl = Label(root, image=bg_img)
bg_img_lbl.place(x=450, y=0)

# Users Table;
mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
                               database="Lifechoices_Online", auth_plugin="mysql_native_password")

mycursor = mydb.cursor()
mycursor.execute("select * from Login")
user = mycursor.fetchall()
tree = ttk.Treeview(root)

# Define the number of columns
tree["columns"] = ("Name", "Id_Number", "Phone_Number", "Email_Address", "Time_in", "Time_out")

# Formatting columns
tree.column("#0", width=75, minwidth=25)
tree.column("Name", anchor=CENTER)
tree.column("Id_Number", anchor=CENTER, width=160)
tree.column("Phone_Number", anchor=CENTER, width=150)
tree.column("Email_Address", anchor=CENTER, width=150)
tree.column("Time_in", anchor=CENTER, width=160)
tree.column("Time_out", anchor=CENTER, width=160)

# Defining the column headings
tree.heading("#0", text="Labels", anchor=CENTER)
tree.heading("Name", text="Username", anchor=CENTER)
tree.heading("Id_Number", text="ID Number", anchor=CENTER)
tree.heading("Phone_Number", text="Mobile", anchor=CENTER)
tree.heading("Email_Address", text="Email Address", anchor=CENTER)
tree.heading("Time_in", text="Time In", anchor=CENTER)
tree.heading("Time_out", text="Time Out", anchor=CENTER)

# From the database
x = 0
for data in user:
    tree.insert(parent="", index="end", iid=x, text="User", values=(data[0], data[1], data[2], data[3], data[4],
                                                                    data[5]))
    x += 1

# Placing the treeview
tree.place(x=0, y=60)

put_in = Button(root, text="INSERT", font=("Ariel", 13), bg="black", fg="#f7f7f7")
put_in.place(x=250, y=350)

take_out = Button(root, text="DELETE", font=("Ariel", 13), bg="black", fg="#f7f7f7")
take_out.place(x=700, y=350)

sign_out = Button(root, text="E X I T", font=("Ariel", 13), bg="black", fg="#f7f7f7")
sign_out.place(x=200, y=750)

sign_in = Button(root, text="SIGN IN", font=("Ariel", 13), bg="black", fg="#f7f7f7")
sign_in.place(x=460, y=750)

out = Button(root, text="SIGN OUT", font=("Ariel", 13), bg="black", fg="#f7f7f7")
out.place(x=730, y=750)

mycursor.execute("select * from Next_Of_Kin")
users = mycursor.fetchall()
tree1 = ttk.Treeview(root)

# Define the number of columns
tree1["columns"] = ("Id", "Name", "Phone_Number", "Id_Number")

# Formatting columns
tree1.column("#0", width=75, minwidth=25)
tree1.column("Id", anchor=CENTER)
tree1.column("Name", anchor=CENTER)
tree1.column("Phone_Number", anchor=CENTER, width=120)
tree1.column("Id_Number", anchor=CENTER, width=150)

# Defining the column headings
tree1.heading("#0", text="Labels", anchor=CENTER)
tree1.heading("Id", text="Row Number", anchor=CENTER)
tree1.heading("Name", text="Name", anchor=CENTER)
tree1.heading("Phone_Number", text="Mobile", anchor=CENTER)
tree1.heading("Id_Number", text="Kin of", anchor=W)

# From the database
x = 0
for data in users:
    tree1.insert(parent="", index="end", iid=x, text="User", values=(data[0], data[1], data[2], data[3]))
    x += 1

# Placing the treeview
tree1.place(x=130, y=450)

# Run the program
root.mainloop()