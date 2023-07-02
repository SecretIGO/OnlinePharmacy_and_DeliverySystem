# library for calculations

def calculate_itemTotal(item_price, qty):
    return item_price * qty

def calculate_itemRating(item_rating1s, item_rating2s, item_rating3s, item_rating4s, item_rating5s, total_numOf_ratings):
    return round(((1*item_rating1s)+(2*item_rating2s)+(3*item_rating3s)+(4*item_rating4s)+(5*item_rating5s))/float(total_numOf_ratings), 2)


    

