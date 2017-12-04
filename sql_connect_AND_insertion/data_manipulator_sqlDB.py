#!/usr/bin/python

import MySQLdb

#csv_parse.py
import csv
from datetime import datetime
with open('2017_12_04.csv') as csvfile:
  reader = csv.reader(csvfile)
  total = 0
  for row in reader:
      print(row[0])
      print(row[1])
      try:
          current = float(row[1]) #this is the kwh value of the current row
          date_time = datetime.strptime(row[0], '%m/%d/%Y %I:%M%p')
      except:
          print

#Connecting to SQLdb
conn = MySQLdb.connect(host = 'weiheliosdashboard.cq6hbz3m95ou.us-east-1.rds.amazonaws.com', 
                               user = 'helios', passwd = 'cleanenergy123')
cursor = conn.cursor()
   
if conn.is_connected():
   print('Successfully connected to SQL database. Initiating data insertion.')
   dataInsert()
else:
   print('Failed to connect to SQL database. Please try again.')


#Inserting scraped and parsed data into SQLdb
def dataInsert():
   try:
      cursor.execute("""INSERT INTO Energy (datetime, EnrgyInterval) VALUES ()""", (row[0], row[1]))
      conn.commit()
      cursor.execute("""SELECT * FROM Energy;""")
      print cursor.fetchall()
      
   except:
      conn.rollback()
      
if __name__ == '__main__':
   dataInsert()
   conn.close()
