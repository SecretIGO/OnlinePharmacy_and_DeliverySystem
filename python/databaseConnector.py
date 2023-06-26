import mysql.connector
import math_utils

fname = "first"
mname = "middle"
lname = "last"

fullName = {
    "firstName" : fname,
    "middleName" : mname,
    "lastName" : lname
}

print(fullName)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database = "db_onphar"
)

print(mydb)

mycursor = mydb.cursor()

name = "courier"
desc = "this user has the ability to view parcel information and delivery address of the package"

sql = ("INSERT INTO roles (rolename, roledescription) VALUES (%s,%s)")
val = (name, desc)

mycursor.execute(sql,val)
mycursor.execute("COMMIT")