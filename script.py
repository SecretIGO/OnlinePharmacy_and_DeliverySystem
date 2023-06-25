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

x = 1

print(x)