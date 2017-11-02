import csv
from datetime import datetime
with open('SunPower_Nov_01_2017_Nov_01_2017.csv') as csvfile:
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