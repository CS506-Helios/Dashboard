class manipulator:

    def __init__(self):
        self.total_kwh = 0 # The total amount of energy produced
        self.price_per_kwh = 0
        self.money_saved = 0 # The amount of money saved on energy by the panel

    # Method to get updates from the database automatically every ten minutes
    def update_total(self):
        '''
        Implementation should allow for the total to update every ten minutes automatically
        The updated total_kwh value will be forwarded using the update_channels method of control.py.
        This way the control can perform all the websocket interaction, and needs only to call this method. contributor
                '''
        recent = self.get_current()
        print('Current: '.format(self.total_kwh))  # TODO: REMOVE
        self.total_kwh += recent
        self.update_money_saved() # Update the total money saved based on the update
        # push the new value for total energy produced to the front end
 
        print('Updated: '.format(self.total_kwh))  # TODO: REMOVE

    # Allows the price of energy to be updated by the admin
    def update_price(self, new_price):
        self.price_per_kwh = new_price
        ''' 
        May want to allow total cost to remain unchanged, only allowing the updated price to affect the energy 
        collected after the price is updated.
        '''

    # Method to take the total and the price of energy and calculate the total amount of money saved so far
    def update_money_saved(self):
        '''
        Updates the total amount of money saved and passes the information to control.py in order to update the
        front end and saves the info to the DB
        '''
        self.money_saved += self.price_per_kwh * self.get_current()
        # Push the new value for money saved to the front end and server

    # Method used to get an estimate of the current energy being produced for the gauge panel
    def get_current(self):
        current = 0 #TODO: replace with query to DB to get the data since the last update
        return current
