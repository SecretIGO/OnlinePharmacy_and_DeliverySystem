def addStore(store_name, store_branch, store_address, mycursor):
  query = "INSERT INTO store (store_name, store_branch, store_address, store_itemsSold, store_rating) VALUES (%s,%s,%s,%s,%s)"
  values = (store_name, store_branch, store_address, 0, 0)
  
  mycursor.execute(query, values)
  mycursor.execute("COMMIT")
