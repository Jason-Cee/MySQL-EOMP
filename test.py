# import mysql.connector
#
# mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
#                                database='LifeChoices_Online', auth_plugin='mysql_native_password')
#
# mycursor = mydb.cursor()
#
# sql = "INSERT INTO User VALUES (Name, Id_Number, Mobile_Number, Email_Address)"
# value = ("Jason Calvert", "9804075027082", "0762562346", "jasondoescoding@gmail.com")
# mycursor.execute(sql, value)
#
# mydb.commit()
#
# print(mycursor.rowcount, "Details recorded.")
# mycursor.execute('Select * from User')
# for i in mycursor:
#     print(i)


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
