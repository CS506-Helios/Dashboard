from django.test import TestCase
import DataCalculator

class DataTests(TestCase):

    def test_total(self):
        total = DataCalculator.total_energy(individial_energy_totals=[5] * 100)
        self.assertEqual(500, total)

    def test_analogy(self):
        analogy = DataCalculator.energy_analogy_value(total_energy=500, energy_unit=100)
        self.assertEqual(analogy, 5)

    def test_money_saved(self):
        saved = DataCalculator.money_saved(total_energy=500, price_per_kwh=1)
        self.assertEqual(saved, 500)

    def test_energy_consumption(self):
        percentage = DataCalculator.energy_percentage(total_energy=500, days=10)
        self.assertEqual(percentage, 10)
