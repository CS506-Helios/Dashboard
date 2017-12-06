import pyodbc
daily_energy_consumption = 5
server = 'weiheliosdashboard.cq6hbz3m95ou.us-east-1.rds.amazonaws.com'
database = 'WEIHeliosDashboard'
username = 'helios'
password = 'cleanenergy123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
#TO DO: Build and return an array which stores the energy value at each row at a separate index in the array
def individial_energy_totals(energy_data):
    totals = [None] * cursor.rowcount()
    row = cursor.fetchone()
    totals[cursor.rownumber()] = row
    return totals

#TO DO: Return the sum of the values at each index of the passed array
def total_energy(individial_energy_totals):
    total = 0
    for sub_total in individial_energy_totals():
        total += sub_total
    return total

#TO DO: Return value obtained by dividing the total energy by the energy unit
def energy_analogy_value(total_energy, energy_unit):
    return total_energy() / energy_unit

#TO DO: Given the total energy produced and the price per KWh, return the money saved
def money_saved(total_energy, price_per_kwh):
    return total_energy() * price_per_kwh

#TO DO: Given the total energy produced and the timescale, use the global variable to calculate
#what percentage of the building's total energy consumption is accounted for by the panels
def energy_percentage(total_energy, timescale, days):
    return total_energy / (daily_energy_consumption * days)