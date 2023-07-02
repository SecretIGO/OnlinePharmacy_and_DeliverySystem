import re

# dbcon_user local lib for accessing data for users

# ______________________________________________________________________________________________ < ' USERS ' >
# - - - - - - - - - - - FINDING USER IN THE DATABASE (signin)

  # problem 1 : not case sensitive...
    # -> eg. testUser and testuser as username is detected as an active username when testUser is the only one in the db
    # FIXED!

def find_username(username, mycursor):

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

  return result

# ______________________________________________________________________________________________
# - - - - - - - - - - - VALIDATE EMAIL (signup)

def validate_email(email):
  # Check if email follows the 'email' pattern
  regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

  if not re.search(regex, email):
    return False
  
  return True

# ______________________________________________________________________________________________
# - - - - - - - - - - - VALIDATE PASSWORD (signup)

def validate_password(password):
  # Check if the password has at least 8 characters
  if len(password) < 8:
    return False
  
  # Check if the password contains at least one uppercase letter
  if not re.search(r'[A-Z]', password):
    return False
  
  # Check if the password contains at least one lowercase letter
  if not re.search(r'[a-z]', password):
    return False
  
  # Check if the password contains at least one digit
  if not re.search(r'\d', password):
    return False
  
  # If all the conditions are met, the password is valid
  return True

# ______________________________________________________________________________________________
# - - - - - - - - - - - ADDING USER TO THE DATABASE (signup)

  # NOTE : signup from main signup screen add role to be automatically 2 for buyer

def addUser(fullname, username, password, email, mycursor):
  try:
    input_username = find_username(username, mycursor)
    
    is_valid = validate_email(email)
    if not is_valid:
      print("invalid email")
      return

    is_valid = validate_password(password)
    if not is_valid:
      print("invalid password")
      return

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

# ______________________________________________________________________________________________
# - - - - - - - - - - - LOGGING IN USER (signin)

  # This works, but according to stackoverflow, comparisons like this is bypassable. but whatever.

def login_user(username, password, mycursor):
  try:
    input_username = find_username(username, mycursor)
    
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

  return True

# ______________________________________________________________________________________________
# - - - - - - - - - - - LOGOUT USER

def logout_user(username, mycursor):
  query = ("UPDATE users SET activeStatus=0 WHERE username = %s")
  mycursor.execute(query, (username,))

  mycursor.execute("COMMIT")
  
# ______________________________________________________________________________________________
# - - - - - - - - - - - GETTING USER INFORMATION

def get_userInformation(username, mycursor):
  query = ("SELECT firstname, middlename, lastname, username, email FROM users WHERE BINARY username=%s")
  mycursor.execute(query, (username,))
  result = mycursor.fetchone()

  if result:
    details = s_fname, s_mname, s_lname, s_username, email = result

  return details

# ______________________________________________________________________________________________
# - - - - - - - - - - - GETTING THE COUNT OF ALL CURRENTLY ONLINE USERS

def get_activeUserCount(mycursor):
  query = ("SELECT COUNT(activeStatus) FROM users WHERE activeStatus = true")
  mycursor.execute(query)
  activeUsers = mycursor.fetchone()[0]

  print("active users : ", activeUsers)

  return activeUsers

# ______________________________________________________________________________________________
# - - - - - - - - - - - GETTING THE COUNT OF ALL USERS

def get_userCount(mycursor):
  query = ("SELECT COUNT(*) FROM users")
  mycursor.execute(query)
  numof_users = mycursor.fetchone()[0]

  print("num of users : ", numof_users)

  return numof_users