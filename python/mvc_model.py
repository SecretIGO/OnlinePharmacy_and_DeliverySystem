# LIBRARIES
import mysql.connector
import datetime

# LOCAL LIBRARIES
import math_utils
import dbcon_user
import dbcon_store

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database = "db_onphar"
)

mycursor = mydb.cursor()

# dbcon_user.get_userCount(mycursor)

# print(dbcon_user.get_roleCount(mycursor))

# dbcon_user.get_allActiveUserCount(1, mycursor)

# dbcon_user.find_username("testUser", 1, mycursor)

# dbcon_store.addStore("samplePharmacy", "Makati", "Chino Roces Ave, Legazpi Village, Makati City, 1223 Metro Manila", mycursor)

# dbcon_user.addUser(("John", "Harvey", "Doe"), "johndoe", "myjohndoeA28", "johndoe@gmail.com", 2, mycursor)

# print(float(math_utils.calculate_itemRating(5,4,8,1,30, 48)))