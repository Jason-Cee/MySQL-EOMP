from tkinter import *
from tkinter import messagebox, ttk

import mysql.connector

# WINDOW
root = Tk()
root.title("Lifechoices Online")  # WINDOW TITLE
root.geometry("1000x800")  # WINDOW SIZE
root.resizable(False, False)  # CAN'T CHANGE SIZE MANUALLY
# Background Image
bg_img = PhotoImage(file="lca.png")
bg_img = bg_img.subsample(5)
bg_img_lbl = Label(root, image=bg_img)
bg_img_lbl.place(x=450, y=0)


def adminregister():
    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                   database='Lifechoices_Online')

    mycursor = mydb.cursor()
    mycursor.execute("Select * from Login")
    tree = ttk.Treeview(root)
    tree['show'] = "headings"
    # define number of columns
    tree["columns"] = ("Name", "Id_Number", "Phone_Number", "Email_Address", "Time_in")

    # assigning properties of columns

    tree.column("Name", width=50, minwidth=50, anchor=CENTER)
    tree.column("Id_Number", width=50, minwidth=50, anchor=CENTER)
    tree.column("Phone_Number", width=100, minwidth=100, anchor=CENTER)
    tree.column("Email_Address", width=100, minwidth=100, anchor=CENTER)
    tree.column("Time_in", width=50, minwidth=50, anchor=CENTER)

    # heading names
    tree.heading("Name", text="Name")
    tree.heading("Id_Number", text="ID Number")
    tree.heading("Phone_Number", text="Phone_Number")
    tree.heading("Email_Address", text="Email Address")
    tree.heading("Time_in", text="Time In")

    i = 0
    for user in mycursor:
        tree.insert('', i, text="", values=(user[0], user[1], user[2], user[3], user[4]))
        i = +1

    v_scroll = ttk.Scrollbar(tree, orient="vertical")
    v_scroll.configure(command=tree.yview)
    tree.configure(yscrollcommand=v_scroll.set)
    v_scroll.pack(fill=Y, side=RIGHT)

    tree.place(x=0, y=70, width=1000, height=150)

    # BLUE FRAME
    frame_left = Frame(root, width=400, height=400, bg="#346ab3")
    frame_left.place(x=100, y=260)
    log = Label(frame_left, text="USER DETAILS", font=("Ariel", 20), bg="#346ab3", fg="#9ccb3b")
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

    # GREEN FRAME
    frame_right = Frame(root, width=400, height=400, bg="#9ccb3b")
    frame_right.place(x=500, y=260)
    reg = Label(frame_right, text="NEXT OF KIN DETAILS", font=("Ariel", 20), bg="#9ccb3b", fg="#346ab3")
    reg.place(x=50, y=10)

    # NAME & SURNAME LABEL AND ENTRY
    users = Label(frame_right, text="Name & Surname:", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3")
    users.place(x=10, y=100)
    users_ent = Entry(frame_right, bg="#346ab3", fg="black")
    users_ent.place(x=210, y=100)

    # MOBILE NUMBER LABEL AND ENTRY
    phones = Label(frame_right, text="Mobile Number:", font=("Ariel", 13), bg="#9ccb3b", fg="#346ab3")
    phones.place(x=10, y=210)
    phones_ent = Entry(frame_right, bg="#346ab3", fg="black")
    phones_ent.place(x=210, y=210)

    def updateA():
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='Lifechoices_Online')
        mycursor = mydb.cursor()
        mycursor.execute("Select * from Login")
        tree = ttk.Treeview(root)
        tree['show'] = "headings"  # otherwise there's going to be an empty first row(don't know why)
        # define number of columns
        tree["columns"] = ("Name", "Id_Number", "Phone_Number", "Email_Address", "Time_in")

        # assigning properties of columns

        tree.column("Name", width=50, minwidth=50, anchor=CENTER)
        tree.column("Id_Number", width=50, minwidth=50, anchor=CENTER)
        tree.column("Phone_Number", width=100, minwidth=100, anchor=CENTER)
        tree.column("Email_Address", width=100, minwidth=100, anchor=CENTER)
        tree.column("Time_in", width=50, minwidth=50, anchor=CENTER)

        # heading names
        tree.heading("Name", text="Name")
        tree.heading("Id_Number", text="ID Number")
        tree.heading("Phone_Number", text="Phone_Number")
        tree.heading("Email_Address", text="Email Address")
        tree.heading("Time_in", text="Time In")

        # For loop
        # allows for the records in "SignInOutTable"
        # to be displayed in the treeview diagram in correct order
        j = 0
        for userA in mycursor:
            tree.insert('', j, text="", values=(userA[0], userA[1], userA[2], userA[3], userA[4], userA[5]))
            j = +1

        scroller = ttk.Scrollbar(tree, orient="vertical")
        scroller.configure(command=tree.yview)
        tree.configure(yscrollcommand=v_scroll.set)
        scroller.pack(fill=Y, side=RIGHT)
        tree.place(x=50, y=70, width=1000, height=150)

    updatebtn = Button(root, text="UPDATE", font=("Ariel", 13), bg="black", fg="#f7f7f7", command=updateA)
    updatebtn.place(x=200, y=700, width=200)

    def deleteA():
        if user_ent.get() == "" or id_num_ent.get() == "":
            messagebox.showerror("ERROR", "IN ORDER TO DELETE YOU NEED TO FILL IN NAME AND ID NUMBER")
        else:
            try:
                mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                               database='Lifechoices_Online')
                mycursor = mydb.cursor()
                mycursor.execute("Select * from Login")
                row = mycursor.fetchone()
                if row == "":
                    messagebox.showerror("Error", "Invalid Name or ID")
                    user.delete(0, END)
                    id_num_ent.delete(0, END)
                else:
                    mycursor.execute(
                        "Delete from Login where Id_Number='" + id_num_ent.get() + "' and Name='" + user_ent.get() + "'")
                    mydb.commit()
                    mydb.close()
                    messagebox.showinfo("SUCCESS",
                                        user.get() + ", HAS BEEN DELETED")
            except ValueError as x:
                pass

    deletebtn = Button(root, text="DELETE", font=("Ariel", 13), bg="black", fg="#f7f7f7", command=deleteA)
    deletebtn.place(x=400, y=700, width=200)

    def insertA():
        if user_ent.get() == "" or id_num_ent.get() == "" or phone_ent.get() == "" or email_ent.get() == "" or \
                users_ent.get() == "" or phones_ent.get() == "":
            messagebox.showerror("Error!", "Please fill in ALL fields")
        else:
            try:
                if len(id_num_ent.get()) != 13 or len(phone_ent.get()) != 10 or len(phones_ent.get()) != 10:
                    print("Invalid Data Type")
                else:
                    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                                   database='Lifechoices_Online')
                    mycursor = mydb.cursor()
                    row = mycursor.fetchone()
                    if row is not None:
                        messagebox.showerror("Error", "This user already exists")
                        user_ent.delete(0, END)
                        id_num_ent.delete(0, END)
                        phone_ent.delete(0, END)
                        email_ent.delete(0, END)
                        users_ent.delete(0, END)
                        phones_ent.delete(0, END)
                    else:
                        mycursor.execute(
                            "INSERT into Login values('" + user_ent.get() + "','" + id_num_ent.get() + "','" + phone_ent.get() +
                            "','" + email_ent.get() + "','" + users_ent.get() + "','" + phones_ent.get() + "');")
                        mydb.commit()
                        mydb.close()
                        messagebox.askquestion("REGISTRATION SUCCESSFUL",
                                               user.get() + " is now Registered on Lifechoices Online")

            except ValueError as x:
                messagebox.showerror("ERROR", "Enter Valid Entries")

    insertbtn = Button(root, text="INSERT", font=("Ariel", 13), bg="black", fg="#f7f7f7", command=insertA)
    insertbtn.place(x=600, y=700, width=200)

    root.mainloop()


if __name__ == '__main__':
    #   function where login style and functions are stored is being called to run
    adminregister()
