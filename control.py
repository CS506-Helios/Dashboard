import manipulator
import datetime
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
class Controller:




    # Query SQL database for data in the given timescale.
    def get_data (timescale):
        engine = create_engine('helios-wei-dashboard.cq6hbz3m95ou.us-east-1.rds.amazonaws.com')
        # The above string argument is the name of the server

        Session = sessionmaker(bind=engine)
        session = Session()
        '''
        Given the new timescale (year, month, week, or day) create a query to the database to retrieve the data for the
        specified period
        '''

        if timescale == 'week':

            now = datetime.datetime.now()
            day = now.date()
            #SQL query to get data for the last 7 days
            for entry in session.query(func.sum('TOTAL KWH')'TIMESTAMP'):
                totals = [None] * 7
                index = now.day() - 'TIMESTAMP DAY OF MONTH'
                if index <= 7 & index > 0:
                    totals[index] += 0 #TODO: replace with the KWH for the entry
                print(entry.field1 + ' ' + entry.field2)


            print 'week query'
            return

        if timescale == 'month':

            now = datetime.datetime.now()
            current_month = now.month
            for entry in session.query(func.sum('KWH')).filter(month = current_month):
                totals = [None] * now.date()
                totals['ENTRY DATE TIMESTAMP' + 1] += 0 #TODO: replace with the KWH for the entry
                #Transmit data in JSON format to AJAX frontend

            print 'month query'
            # SQL query to request data for the month starting at the first of the month.
            return

        if timescale == 'year':
            now = datetime.datetime.now()
            year = now.year

            # SQL query to request data from the past 365 days
            for entry in session.query('TIMESTAMP').filter('TIMESTAMP YEAR' == year):
                #Transmit data in JSON format to AJAX front end
                totals = [None] * 12
                totals['ENTRY TIMESTAMP MONTH'+1] += 0 #TODO: replace with the KWH for the entry

            print 'year query'
            return

        if timescale == None:
            return
        #Call should be made to update_total
        manipulator.update_total()
        print('implement get_data') # TODO: REMOVE
        return

    # Responds to a client's request to change the timescale that they are viewing
    def change_timescale(self, new_timescale):
        '''
        given the new timescale, call get_data(timescale) to create a query for the database structured to retrieve
            that time frame
        update websocket channels to reflect the new time frame, while allowing other websocket channels to
            remain unaltered
        '''
        self.get_data(new_timescale)
        self.update_channels()

        print('implement chenge_timescale') # TODO: REMOVE

    '''
    This method is used to facilitate administrator login.
    '''
    def login(self, username, password):
        '''
        Look up  username in SQL Database and check that the password for that username entry matches
        the password provided. This will likely be implemented by using the Webdriver library
        '''
        # TODO: query database to find username, and check that the password matches.
        if 'username is not in database':
            return 0
        username_password = 'entry that will be retrieved from the database if the username exists'
        if password == username_password:
            return 1
        else:
            return 0
        print('implement login') # TODO: REMOVE

    # Parses updates from the dashboard editor and updates the values in the database
    def update_admin_settings(self):
        '''
        parse info given by the front end
        find user in database
        save to database (only save if values are different)
        '''
        print('implement update_admin_settings') # TODO: REMOVE

    # Allows the price of energy to be updated by the admin
    def update_price(self, new_price):
        manipulator.price_per_kwh = new_price
        ''' 
        May want to allow total cost to remain unchanged, only allowing the updated price to affect the energy 
        collected after the price is updated.
        '''

