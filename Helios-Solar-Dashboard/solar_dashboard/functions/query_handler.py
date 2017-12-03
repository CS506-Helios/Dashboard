import pyodbc
from django.http import HttpResponse #remove
from django.http import JsonResponse #remove

server = 'weiheliosdashboard.cq6hbz3m95ou.us-east-1.rds.amazonaws.com'
database = 'WEIHeliosDashboard'
username = 'helios'
password = 'cleanenergy123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#Handles the queries required to retrieve dashboard initialization data
def initialize():
    result = {}

    #Get the timescale setting
    timescale_query = "SELECT * FROM DashboardSettings;"
    cursor.execute(timescale_query)
    row = cursor.fetchone()
    result['timescale'] = row[0]

    #Get energy analogy settings
    energy_analogy_query = "SELECT * FROM EnergyAnalogy;"
    cursor.execute(energy_analogy_query)
    row = cursor.fetchone()
    result['string1'] = row[0]
    result['string2'] = row[1]
    result['imageURL'] = row[3]

    return result