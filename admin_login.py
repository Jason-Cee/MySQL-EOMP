# import datetime
# from tkinter import *
# from tkinter import ttk, messagebox
# import mysql.connector
# from admin import adminregister
#
# root = Tk()
# root.title("Lifechoices Online")  # WINDOW TITLE
# root.geometry("1000x800")  # WINDOW SIZE
# root.resizable(False, False)  # CAN'T CHANGE SIZE MANUALLY
# # Background Image
# bg_img = PhotoImage(file="lca.png")
# bg_img = bg_img.subsample(5)
# bg_img_lbl = Label(root, image=bg_img)
# bg_img_lbl.place(x=450, y=0)
#
#
# def draw_admin():
#     lbl_title = Label(root, text="Life Choices Online", fg="#71D696", bg="#EBFFEC", font="Purisa 40 bold")
#     lbl_title.place(x=100, y=20)
#     lbl_admin = Label(root, text="Admin", fg="#71D696", bg="#EBFFEC", font="Purisa 30 bold")
#     lbl_admin.place(x=280, y=130)
#
#     mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
#                                    database='Lifechoices_Online')
#
#     mycursor = mydb.cursor()
#
#     # Calender to choose a date from
#     # Making variables to hold current year, month and date to allow flexibility in calendar
#     # x = datetime.datetime.now()
#     # year = x.year
#     # month = x.month
#     # day = x.day
#     #
#     # cal = Calendar(admin, selectmode='day',
#     #                year=year, month=month,
#     #                day=day)
#     # cal.place(x=50, y=250, width=250, height=200)
#
#     def search():
#
#         lbl_title.config(text="")
#         lbl_admin.config(text="")
#         # TO CHECK ALL THAT HAS SIGNED IN
#         mycursor.execute("select "
#                          " Date,ID_No, Name, In_Out, Time"
#                          " from SignInOutTable where Date='" + "' and Name='" + stvar.get() + "'")
#
#         tree_search = ttk.Treeview(root)
#         tree_search['show'] = "headings"  # otherwise there's going to be an empty first row(don't know why)
#         # define number of columns
#         tree_search["columns"] = ("Date", "ID_No", "Name", "Sign In/Out", "Time")
#
#         # assigning properties of columns
#         tree_search.column("Date", width=100, minwidth=100, anchor=CENTER)
#         tree_search.column("ID_No", width=120, minwidth=120, anchor=CENTER)
#         tree_search.column("Name", width=120, minwidth=120, anchor=CENTER)
#         tree_search.column("Sign In/Out", width=50, minwidth=50, anchor=CENTER)
#         tree_search.column("Time", width=50, minwidth=50, anchor=CENTER)
#
#         # heading names
#         tree_search.heading("Date", text="Date")
#         tree_search.heading("ID_No", text="ID_No")
#         tree_search.heading("Name", text="Name")
#         tree_search.heading("Sign In/Out", text="Sign In/Out")
#         tree_search.heading("Time", text="Time")
#
#         # For loop
#         # allows for the records in "SignInOutTable"
#         # to be displayed in the treeview diagram in correct order
#         z = 0
#         for userA in mycursor:
#             tree_search.insert('', z, text="", values=(userA[0], userA[1], userA[2], userA[3], userA[4]))
#             z = +1
#
#         tree_search.place(x=50, y=70, width=650, height=150)
#
#     def sign_in():
#         lbl_title.config(text="")
#         lbl_admin.config(text="")
#         # TO CHECK ALL THAT HAS SIGNED IN
#         mycursor.execute("select "
#                          " max(Date) Date,max(ID_No) ID_No, Name,"
#                          " if(In_Out = 1, 'Signed In', 'Signed Out') Sign_In_Out, max(Time) Time"
#                          " from SignInOutTable where In_Out = 1 and Date=curdate()"
#                          " group by Date, Name;")
#
#         tree_in = ttk.Treeview(root)
#         tree_in['show'] = "headings"  # otherwise there's going to be an empty first row(don't know why)
#         # define number of columns
#         tree_in["columns"] = ("Date", "ID_No", "Name", "Sign In/Out", "Time")
#
#         # assigning properties of columns
#         tree_in.column("Date", width=100, minwidth=100, anchor=CENTER)
#         tree_in.column("ID_No", width=120, minwidth=120, anchor=CENTER)
#         tree_in.column("Name", width=120, minwidth=120, anchor=CENTER)
#         tree_in.column("Sign In/Out", width=50, minwidth=50, anchor=CENTER)
#         tree_in.column("Time", width=50, minwidth=50, anchor=CENTER)
#
#         # heading names
#         tree_in.heading("Date", text="Date")
#         tree_in.heading("ID_No", text="ID_No")
#         tree_in.heading("Name", text="Name")
#         tree_in.heading("Sign In/Out", text="Sign In/Out")
#         tree_in.heading("Time", text="Time")
#
#         # For loop
#         # allows for the records in "SignInOutTable"
#         # to be displayed in the treeview diagram in correct order
#         for userA in mycursor:
#             tree_in.insert('', userA[6], text="", values=(userA[0], userA[1], userA[2], userA[3], userA[4], userA[5]))
#
#         tree_in.place(x=50, y=70, width=700, height=150)
#     # ENDS HERE
#
#     def sign_out():
#         lbl_title.config(text="")
#         lbl_admin.config(text="")
#         # TO CHECK ALL THAT HAS SIGNED OUT
#         mycursor.execute("select "
#                          " max(Date) Date,max(ID_No) ID_No, max(Name) Name,"
#                          " if(In_Out = 1, 'Signed In', 'Signed Out') Sign_In_Out, max(Time) Time"
#                          " from SignInOutTable where In_Out = 0 and Date=curdate()"
#                          "group by Time;")
#
#         tree_out = ttk.Treeview(root)
#         tree_out['show'] = "headings"  # otherwise there's going to be an empty first row(don't know why)
#         # define number of columns
#         tree_out["columns"] = ("Date", "ID_No", "Name", "Sign In/Out", "Time")
#
#         # assigning properties of columns
#         tree_out.column("Date", width=100, minwidth=100, anchor=CENTER)
#         tree_out.column("ID_No", width=120, minwidth=120, anchor=CENTER)
#         tree_out.column("Name", width=120, minwidth=120, anchor=CENTER)
#         tree_out.column("Sign In/Out", width=50, minwidth=50, anchor=CENTER)
#         tree_out.column("Time", width=50, minwidth=50, anchor=CENTER)
#
#         # heading names
#         tree_out.heading("Date", text="Date")
#         tree_out.heading("ID_No", text="ID_No")
#         tree_out.heading("Name", text="Name")
#         tree_out.heading("Sign In/Out", text="Sign In/Out")
#         tree_out.heading("Time", text="Time")
#
#         # For loop
#         # allows for the records in "SignInOutTable"
#         # to be displayed in the treeview diagram in correct order
#         x = 0
#         for userA in mycursor:
#             tree_out.insert('', x, text="", values=(userA[0], userA[1], userA[2], userA[3], userA[4]))
#             x = +1
#
#         tree_out.place(x=50, y=70, width=700, height=150)
#         # ENDS HERE
#
#     def register():
#         lbl_title.config(text="")
#         lbl_admin.config(text="")
#         btn_search.destroy()
#         mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
#                                        database='Lifechoices_Online')
#
#         mycursor = mydb.cursor()
#         mycursor.execute("Select Name, Surname, ID_No, Contact, NextOfKinName, NextOfKinContact , id from Register")
#         tree_insert = ttk.Treeview(root)
#         tree_insert['show'] = "headings"  # otherwise there's going to be an empty first row(don't know why)
#         # define number of columns
#         tree_insert["columns"] = ("Name", "Surname", "ID No", "Contact No", "NextOfKin Name", "NextOfKin Contact")
#
#         # assigning properties of columns
#         tree_insert.column("Name", width=50, minwidth=50, anchor=CENTER)
#         tree_insert.column("Surname", width=50, minwidth=50, anchor=CENTER)
#         tree_insert.column("ID No", width=100, minwidth=100, anchor=CENTER)
#         tree_insert.column("Contact No", width=100, minwidth=100, anchor=CENTER)
#         tree_insert.column("NextOfKin Name", width=50, minwidth=50, anchor=CENTER)
#         tree_insert.column("NextOfKin Contact", width=100, minwidth=100, anchor=CENTER)
#
#         # heading names
#         tree_insert.heading("Name", text="Name")
#         tree_insert.heading("Surname", text="Surname")
#         tree_insert.heading("ID No", text="ID No")
#         tree_insert.heading("Contact No", text="Contact No")
#         tree_insert.heading("NextOfKin Name", text="NextOfKin Name")
#         tree_insert.heading("NextOfKin Contact", text="NextOfKin Contact")
#
#         # For loop
#         # allows for the records in "SignInOutTable"
#         # to be displayed in the treeview diagram in correct order
#         for userA in mycursor:
#             tree_insert.insert('', userA[6], text="", values=(userA[0], userA[1], userA[2], userA[3], userA[4],
#                                                               userA[5]))
#
#         v_scroll = ttk.Scrollbar(tree_insert, orient="vertical")
#         v_scroll.configure(command=tree_insert.yview)
#         tree_insert.configure(yscrollcommand=v_scroll.set)
#         v_scroll.pack(fill=Y, side=RIGHT)
#
#         tree_insert.place(x=50, y=70, width=700, height=150)
#
#     def edit():
#         root.destroy()
#         adminregister()
#
#     def exitApplication():
#         msg = messagebox.askquestion("EXIT", "Are you sure you want to exit?")
#         if msg == "yes":
#             root.destroy()
#         else:
#             pass
#
#     ######################
#     my_list = []
#     stvar = StringVar(root)
#     stvar.set(['Choose Name'])
#
#     mycursor.execute("Select name from Register group by name having count(*)")
#     i = 0
#     for user in mycursor:
#         my_list.append(user[0])
#         i = +1
#     print(my_list)
#     menu = OptionMenu(root, stvar, *my_list, command=None)
#     menu.config(fg="#71D696", bg="#EBFFEC", font="Arial 18 bold")
#     menu["menu"].config(fg="#71D696", bg="#EBFFEC", font="Arial 15")
#     menu.place(x=330, y=305, width=230)
#     name_of_person = stvar.get()
#     ######################
#     btn_register = Button(root, text="Register", fg="#206F3D", bg="#71D696", font="Arial 25 bold", command=register)
#     btn_register.place(x=570, y=360, width=200)
#     btn_signIn = Button(root, text="Signed-In", fg="#206F3D", bg="#71D696", font="Arial 25 bold", command=sign_in)
#     btn_signIn.place(x=570, y=430, width=200)
#     btn_signOut = Button(root, text="Signed-Out", fg="#206F3D", bg="#71D696", font="Arial 25 bold", command=sign_out)
#     btn_signOut.place(x=570, y=500, width=200)
#     btn_search = Button(root, text="Search", fg="#206F3D", bg="#71D696", font="Arial 25 bold", command=search)
#     btn_search.place(x=570, y=300, width=200)
#     btn_edit = Button(root, text="Edit", fg="#206F3D", bg="#71D696", font="Arial 25 bold", command=edit)
#     btn_edit.place(x=570, y=560, width=200)
#
#     mycursor.execute("Select Count(*) from SignInOutTable where Date=curdate() and In_Out=1;")
#     test_g = PhotoImage(file="green.png")
#     img_g = Label(bg="white", border="0", image=test_g)
#     img_g.image = test_g
#     img_g.place(x=50, y=640, width=50, height=50)
#     lbl_g = Button(root, highlightthickness=0, text="", fg="white", bd="0", font="Arial 20 bold", bg="#a8d484")
#     lbl_g.place(x=60, y=650, width=30, height=30)
#     lbl_active = Label(root, text="Users Signed In", fg="#206F3D", bg="#EBFFEC", font="Arial 20 bold")
#     lbl_active.place(x=110, y=650)
#
#     for n in mycursor:
#         lbl_g.config(text=n)
#
#     btn_exit = Button(root, text="Exit", bg="grey", fg="#EBFFEC", font="Arial 25 bold", command=exitApplication)
#     btn_exit.place(x=570, y=720, width=200)
#
#     root.mainloop()
#
#
# if __name__ == '__main__':
#     draw_admin()
