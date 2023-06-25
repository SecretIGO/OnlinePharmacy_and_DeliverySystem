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
  password="",
  database = "db_onphar"
)

print(mydb)

mycursor = mydb.cursor()

name = "admin"
desc = "this user has the ability to view and manage website activities and also view all users"

sql = ("INSERT INTO role (rolename, roledescription) VALUES (%s,%s)")
val = (name, desc)

mycursor.execute(sql, val)

x = 1

print(x)