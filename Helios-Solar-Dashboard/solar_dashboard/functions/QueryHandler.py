import pyodbc

server = 'weiheliosdashboard.cq6hbz3m95ou.us-east-1.rds.amazonaws.com'
database = 'WEIHeliosDashboard'
username = 'helios'
password = 'cleanenergy123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#Handles the queries required to retrieve dashboard initialization data
#Return: Dict containing the initializer data
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

#Desc: Handles the query required to retrive authentication data
#Return: Array containing username and password combo for the username passed.
#Returns null if the username does not exist
def authenticate(username):
    username_query = '''SELECT * FROM AccountDetails
                        WHERE username = \'''' + username + '\';'
    cursor.execute(username_query)
    return cursor.fetchone()

def energy_data(days, timescale):
    energy_data_query =''

    #Determine the query to be made
    if timescale == 'week' or timescale == 'month':
        energy_data_query = '''SELECT SUM(intervalEnergy)
                               FROM EnergyData
                               WHERE ABS(DATEDIFF(day, GETDATE(), time)) <= ''' + str(days) + '''
                               GROUP BY CAST(time AS DATE);'''
    elif timescale == 'year':
        energy_data_query = '''SELECT SUM(intervalEnergy)
                               FROM EnergyData
                               WHERE ABS(DATEDIFF(month, GETDATE(), time)) <= ''' + str(days) + '''
                               GROUP BY DATEPART(month, time);'''
        
    #Execute the query and return the result
    cursor.execute(energy_data_query)  
    return cursor

def energy_analogy():
    energy_analogy_query = "SELECT energyUnit FROM EnergyAnalogy;"
    cursor.execute(energy_analogy_query)
    row = cursor.fetchone()
    return row[0]

def energy_price():
    energy_price_query = "SELECT pricePerKWh from DashboardSettings;"
    cursor.execute(energy_price_query)
    row = cursor.fetchone()
    return row[0]