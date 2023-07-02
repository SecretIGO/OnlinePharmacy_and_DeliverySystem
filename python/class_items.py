# LIBRARIES
from datetime import date
from flask import Flask, render_template, Response, request

# LOCAL LIBRARIES
import math_utils
from databaseConnector import mydb

class items:
    __i_name = ""
    __i_price = 0
    __i_category = ""
    __i_MAXqty = 0
    __i_stockRemaining = 0
    __i_description = ""
    __i_dateListed = ""
    __i_rating = 0.0
    __i_activeStatus = False
    __i_itemsSold = 0

    def __init__(self, name, price, category, MAXqty, description, activeStatus):
        self.__i_name = name
        self.__i_price = price
        self.__i_category = category
        self.__i_MAXqty = MAXqty
        self.__i_description = description
        self.__i_activeStatus = activeStatus

        self.__i_dateListed = date.today()
        self.__i_stockRemaining = self.__i_MAXqty
        self.__i_rating = 0.0
        self.__i_itemsSold = 0

    def get_ItemDetails(self):

        
