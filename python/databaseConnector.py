import mysql.connector
import datetime

# LOCAL LIBRARIES
import math_utils

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database = "db_onphar"
)

# ______________________________________________________________________________________________ < ' USERS ' >
# - - - - - - - - - - - FINDING USER IN THE DATABASE (signin)

  # problem 1 : not case sensitive...
    # -> eg. testUser and testuser as username is detected as an active username when testUser is the only one in the db
    # FIXED!

def find_username(username):
  mycursor = mydb.cursor()

  try:
    query = ("SELECT username FROM users WHERE BINARY username=%s")
    mycursor.execute(query, (username,))
    result = mycursor.fetchone()

    if result:
      print("User found!")
    else:
      print("User does not exist!")

  except Exception as e:
    print("Error exception : ", e)

  finally:
    mydb.close

  return result

# ______________________________________________________________________________________________
# - - - - - - - - - - - ADDING USER TO THE DATABASE (signup)

  # NOTE : signup from main signup screen add role to be automatically 2 for buyer

def addUser(fullname, username, password,email):
  mycursor = mydb.cursor()

  try:
    input_username = find_username(username)
    
    if input_username:
      print("user already exists")
    else:
      print("adding user into the database")
      query = ("INSERT INTO users (firstname, middlename, lastname, username, password, email, id_role, activeStatus) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
      val = (fullname[0], fullname[1], fullname[2], username, password, email, 2, 1)

      mycursor.execute(query, val)
      mycursor.execute("COMMIT")

  except Exception as e:
    print("Exception error : ", e)
  
  finally:
    mydb.close()

# ______________________________________________________________________________________________
# - - - - - - - - - - - LOGGING IN USER (signin)

  # This works, but according to stackoverflow, comparisons like this is bypassable. but whatever.

def login_user(username, password):
  mycursor = mydb.cursor()

  try:
    input_username = find_username(username)
    
    if input_username:
      query = ("SELECT password FROM users WHERE username=%s")
      mycursor.execute(query, input_username)      
      temp_password = mycursor.fetchone()[0]

      if password == temp_password:
        print("User identified!")
        query = ("UPDATE users SET activeStatus=1 WHERE username = %s")
        mycursor.execute(query, (username,))

        mycursor.execute("COMMIT")
      else:
        print("Incorrect password!")
        return False
      
    else:
      print("Username not found!")
      return False

  except Exception as e:
    print("Error Exception : ", e)

  finally:
    mydb.close()

  return True

# ______________________________________________________________________________________________
# - - - - - - - - - - - LOGOUT USER

def logout_user(username):
  mycursor = mydb.cursor()

  query = ("UPDATE users SET activeStatus=0 WHERE username = %s")
  mycursor.execute(query, (username,))

  mycursor.execute("COMMIT")
  
# ______________________________________________________________________________________________
# - - - - - - - - - - - GETTING USER INFORMATION

def get_userInformation(username):
  mycursor = mydb.cursor()

  query = ("SELECT firstname, middlename, lastname, username, email FROM users WHERE BINARY username=%s")
  mycursor.execute(query, (username,))
  result = mycursor.fetchone()

  if result:
    details = s_fname, s_mname, s_lname, s_username, email = result

  return details

# ______________________________________________________________________________________________
# - - - - - - - - - - - GETTING THE COUNT OF ALL CURRENTLY ONLINE USERS

def get_activeUserCount():
  mycursor = mydb.cursor()

  query = ("SELECT COUNT(activeStatus) FROM users WHERE activeStatus = true")
  mycursor.execute(query)
  activeUsers = mycursor.fetchone()[0]

  print("active users : ", activeUsers)

  mydb.close()

  return activeUsers

# ______________________________________________________________________________________________
# - - - - - - - - - - - GETTING THE COUNT OF ALL USERS

def get_userCount():
  mycursor = mydb.cursor()

  query = ("SELECT COUNT(*) FROM users")
  mycursor.execute(query)
  numof_users = mycursor.fetchone()[0]

  print("num of users : ", numof_users)

  mydb.close()

  return numof_users

# ______________________________________________________________________________________________ ' ITEMS '
# - - - - - - - - - - - CALCULATING ITEM PRICE

# def get_itemPrice_byQty(item, qty):
#   query = ("SELECT ")
