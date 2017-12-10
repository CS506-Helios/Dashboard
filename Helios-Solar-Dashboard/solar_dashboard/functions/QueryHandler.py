import pyodbc

server = 'weiheliosdashboard.cq6hbz3m95ou.us-east-1.rds.amazonaws.com'
database = 'WEIHeliosDashboard'
username = 'helios'
password = 'cleanenergy123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#Desc: Handles the queries required to retrieve dashboard initialization data
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

#Desc: Handles the query required to retrieve the energy data
#Param - days: The number of days prior to today for which energy data needs to be retrieved
#Param - timescale: String representing the timescale of the dashboard (week/month/year)
#Return: Cursor object with query results
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

#Desc: Handles the query required to retrieve the amount of energy needed to
#complete the energy analogy action
#Return: Number representing the amount of energy needed to complete the action
def energy_analogy():
    energy_analogy_query = "SELECT energyUnit FROM EnergyAnalogy;"
    cursor.execute(energy_analogy_query)
    row = cursor.fetchone()
    return row[0]

#Desc: Handles the query required to retrieve the price of energy
#Return: Number representing the price per KWh of energy
def energy_price():
    energy_price_query = "SELECT pricePerKWh from DashboardSettings;"
    cursor.execute(energy_price_query)
    row = cursor.fetchone()
    return row[0]

#Desc: Handles the queries required to update the dashboard with the values
#entered in the dashboard editor form
def update_dashboard_settings(form):
    #Build dashboard settings update query
    dashboard_settings_query = "UPDATE DashboardSettings SET"

    #Create flag to determine if dashboard settings neeed to be updated
    update_dashboard = False
    
    if form['cycle']:
        update_dashboard = True
        dashboard_settings_query += " timescale = '" + form['cycle'] + "'"

    if form['price']:
        if update_dashboard:
            dashboard_settings_query += ","
        update_dashboard = True
        dashboard_settings_query += " pricePerKWh = " + form['price']
    
    if update_dashboard:
        dashboard_settings_query += ";"
        cursor.execute(dashboard_settings_query)
        cursor.commit()

    #Build energy analogy update query
    energy_analogy_query = "UPDATE EnergyAnalogy SET"

    #Create flag to determine if energy analogy needs to be updated
    update_energy_analogy = False

    if form['before']:
        update_energy_analogy = True
        energy_analogy_query += " string1 = '" + form['before'] + "'"

    if form['after']:
        if update_energy_analogy:
            energy_analogy_query += ","
        update_energy_analogy = True
        energy_analogy_query += " string2 = '" + form['after'] + "'"
    
    if form['needed']:
        if update_energy_analogy:
            energy_analogy_query += ","
        update_energy_analogy = True
        energy_analogy_query += " energyUnit = " + form['needed']

    if form['url']:
        if update_energy_analogy:
            energy_analogy_query += ","
        update_energy_analogy = True
        energy_analogy_query += " imageURL = '" + form['url'] +  "'" 
    
    if update_energy_analogy:
        energy_analogy_query += ";"
        cursor.execute(energy_analogy_query)
        cursor.commit()