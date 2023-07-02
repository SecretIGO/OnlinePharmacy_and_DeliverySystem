import mysql.connector
import datetime

# LOCAL LIBRARIES
import math_utils
import dbcon_user

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database = "db_onphar"
)

mycursor = mydb.cursor()

# dbcon_user.addUser(("Mark", "Hello", "Robert"), "markRover12", "fridgeofA25", "markemail@gmail.com", mycursor)

# print(float(math_utils.calculate_itemRating(5,4,8,1,30, 48)))