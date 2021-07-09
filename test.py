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
    print(i)
