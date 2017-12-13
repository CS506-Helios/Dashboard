#!/usr/bin/env python

import requests
from datetime import datetime
from decimal import *
import time

# IP address of inverter
host = "144.92.98.92"
# number of seconds between samples
sample_seconds = 60 * 5

    

import pyodbc

#SQL server connection
server = 'weiheliosdashboard.cq6hbz3m95ou.us-east-1.rds.amazonaws.com'
database = 'WEIHeliosDashboard'
username = 'helios'
password = 'cleanenergy123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()



def main():
    energy_generated()
    EnergyData_insertion()

#Inserting scraped solar energy data
def EnergyData_insertion():
    print("started")
    while True:
        try:
            energy = energy_generated()

            now = time.strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute('''insert into EnergyData values(? , ?)''', (now, energy))
            cnxn.commit()
            cursor.execute('''select * from EnergyData;''')
            results = cursor.fetchall()
    
        except requests.exceptions.ConnectTimeout:
            print("Connect timeout at %s" % time.strftime("%H:%M:%S"))
        if sample_seconds > 0:
            time.sleep(sample_seconds)
        else:
            return



# power generated in certain time piriod
def energy_generated():
    url = "http://" + host + "/solar_api/v1/GetInverterRealtimeData.cgi?Scope=System"
    r = requests.get(url, timeout=10)
    json_data = r.json()
    dic = json_data["Body"]["Data"]["PAC"]["Values"]
    # sum up values in two units of inverters and transfer the unit to kWh
    result = sum(dic.values()) / float(12000)
    return result


if __name__ == "__main__":
    main()
