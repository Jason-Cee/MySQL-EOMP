# JASON CALVERT MYSQL END OF MODULE PROJECT

# IMPORTS
import mysql.connector
from tkinter import *
from tkinter import PhotoImage


mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                               database='LifeChoices_Online', auth_plugin='mysql_native_password')

mycursor = mydb.cursor()


class FirstPage:

    def __init__(self, window):
        self.window = window
        self.window.title("Life Choices Online")
        self.window.geometry("600x600")
        self.window.resizable(False, False)
        self.window.config(bg="white")
        # IMAGE
        self.img = PhotoImage(file="lca1.png")
        Label(root, image=self.img).place(x=85, y=10)

        self.window.mainloop()


root = Tk()
run = FirstPage(root)
