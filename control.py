import manipulator
import sched, time
class Controller:
    # Responds to a new websocket channel being opened
    def open_channel(self):
        # Send the data that is required by the new channel
        '''
        Given the set default timescale, query the database and forward that data to the websocket, for the user to view
        '''

        print('implement open_channel') # TODO: REMOVE

    # Push updated data to all websocket clients every ten minutes
    def update_channels(self):
        '''
        Each time that new data is gathered push it along all open channels so thateach has access to the
        new information
        '''
        self.get_data()
        print('implement update_channels') # TODO: REMOVE

    # Query SQL database for data in the given timescale.
    def get_data (timescale):
        '''
        Given the new timescale (year, month, week, or day) create a query to the database to retrieve the data for the
        specified period
        '''
        if timescale == 'day':
            #SQL query to get data from the server, starting at midnight of the current day
            print 'day query'
            return
        if timescale == 'week':
            #SQL query to get data for the last 7 days
            print 'week query'
            return
        if timescale == 'month':
            print 'month query'
            # SQL query to request data for the month starting at the first of the month.
            return
        if timescale == 'year':
            # SQL query to request data from the past 365 days
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

