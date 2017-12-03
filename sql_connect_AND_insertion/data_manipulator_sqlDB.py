#!/usr/bin/python

import MySQLdb
import mysql.connector
from mysql.connector import Error
import csv_parse

#Connecting to SQLDB
def connect():
   try:
      conn = mysql.connector.connect(host = 'localhost', database = 'dashboard', user = 'TBD', password = 'TBD')
      if conn.is_connected():
         print('Successfully connected to SQL database. Initiating data insertion.')
         
    except Error:
       print('Failed to connect to SQL database. Please try again.')
        
    finally:
       conn.close()
       
#Data Insertion function
def dataInsert():
   try:
   

if __name__ == '__main__'
   connect()
