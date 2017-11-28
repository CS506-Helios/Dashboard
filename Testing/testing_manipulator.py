#This has been created by Ben
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
        recent = self.get_current() #variable to hold the amount of energy
        print('Current: '.format(self.total_kwh))  # TODO: REMOVE
        self.total_kwh += recent
        self.update_money_saved() # Update the total money saved based on the update
        # push the new value for total energy produced to the front end
        print('Updated: '.format(self.total_kwh))  # TODO: REMOVE

    # Method to take the total and the price of energy and calculate the total amount of money saved so far
    def update_money_saved(self):
        '''
        Updates the total amount of money saved and passes the information to control.py in order to update the
        front end and saves the info to the DB
        '''
        self.money_saved += self.price_per_kwh * self.get_current()
        # TODO: Push the new value for money saved to the front end and server

    # Method used to get an estimate of the current energy being produced for the gauge panel
    def get_current(self):
        current = 0 # TODO: replace with query to DB to get the data since the last update
        return current

    '''
    This function is used to calculate the "energy fact" that will be saved. The admin will have the ability to change
    the exact nature of the fact, but the calculation will be done here
    '''
    def energy_fact(self, fact_unit, fact_power_requirement):
        return fact_power_requirement * self.total_kwh

    '''
    Calculate the percent of the building's required energy use that is eliminated by the energy produced by the solar
    panels
    '''
    def gauge_percent_calculator(self, building_consumption, energy_produced):
        return energy_produced/building_consumption

#Importing Django UnitTesting
import unittest

class ManipulatorTestCase(unittest.TestCase):
  def test_constructor(self):
    total_kwh = 1
    price_per_kwh = 1
    money_saved = 1
    self.failUnlessRaises(ValueError, manipulator, total_kwh)
    self.failUnlessRaises(ValueError, manipulator, price_per_kwh)
    self.failUnlessRaises(ValueError, manipulator, money_saved)

  def manipulatorSetUp(self):
    manipulator.objects.
  def test_update_total(self):
    self.assertEqual(.get_current, 0)
    self.assertEqual(.update_total
  
  def test_update_money_saved
                     
if __name__ == '__main__':
  unittest.main()
