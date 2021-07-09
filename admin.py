# JASON CALVERT MYSQL END OF MODULE PROJECT

from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import ttk

# IMPORTS
import mysql.connector

# WINDOW
root = Tk()
root.title("Lifechoices Online")  # WINDOW TITLE
root.geometry("1000x800")  # WINDOW SIZE
root.resizable(False, False)  # CAN'T CHANGE SIZE MANUALLY

# LIFECHOICES IMAGE / LOGO
img = PhotoImage(file="lca.png")
Label(root, image=img).place(x=150, y=0)  # IMAGE / LOGO PLACEMENT

mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
                               database="Lifechoices_Online", auth_plugin="mysql_native_password")
mycursor = mydb.cursor()
z = mycursor.execute("Select * from Login")
window = ttk.Treeview(root)

window["columns"] = ("Name", "Phone_Number")

window.column("#0", width=0, minwidth=0, stretch=NO)
window.column("Name", anchor=W, width=200)
window.column("Phone_Number", anchor=W, width=200)

window.heading("#0", text='', anchor=CENTER)
window.heading("Name", text="Name", anchor=CENTER)
window.heading("Phone_Number", text="Phone Number", anchor=CENTER)

x = 0
for data in mycursor:
    window.insert(parent='', index='end', iid=x, text="", values=(data[0], data[1]))
    x += 1

window.pack(pady=20)

root.mainloop()
