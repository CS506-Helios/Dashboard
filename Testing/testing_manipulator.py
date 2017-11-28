import unittest
import manipulator

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
