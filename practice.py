import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="sms",auth_plugin='mysql_native_password')
if con.is_connected():
    print("Connected")
else:
    print("Not Connected")
