import manipulator, sched, time
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

        print('implement update_channels') # TODO: REMOVE

    # Query SQL database for data in the given timescale.
    def get_data (timescale):
        '''
        Given the new timescale (year, month, week, or day) create a query to the database to retrieve the data for the
        specified period
        '''
        if timescale == 'day':
            #SQL query to get data from the server, starting at midnight of the current day
            return
        if timescale == 'week':
            #SQL query to get data for the last 7 days
            return
        if timescale == 'month':
            #SQL query to request data for the month starting at the first of the month.
        if timescale == 'year':
            #SQL query to request data from the past 365 days
        print('implement get_data') # TODO: REMOVE

    # Responds to a client's request to change the timescale that they are viewing
    def change_timescale(new_timescale):
        '''
        given the new timescale, call get_data(timescale) to create a query for the database structured to retrieve
            that time frame
        update websocket channels to reflect the new time frame, while allowing other websocket channels to
            remain unaltered
        '''
        get_data(new_timescale)
        print('implement chenge_timescale') # TODO: REMOVE

    '''
    This method is used to facilitate administrator login.
    '''
    def login(username, password):


        '''
        Look up  username in SQL Database and check that the password for that username entry matches
        the password provided. This will likely be implemented by using the Webdriver library
        '''


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
        price_per_kwh = new_price
        ''' 
        May want to allow total cost to remain unchanged, only allowing the updated price to affect the energy 
        collected after the price is updated.
        '''

