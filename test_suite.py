from django.test import TestCase
import data


class DataTests(TestCase):

    def test_total(self):
        total = data.total_energy(individial_energy_totals=[5] * 100)
        self.assertEqual(500, total)

    def test_analogy(self):
        analogy = data.energy_analogy_value(total_energy=500, energy_unit=100)
        self.assertEqual(analogy, 5)

    def test_money_saved(self):
        saved = data.money_saved(total_energy=500, price_per_kwh=1)
        self.assertEqual(saved, 500)

    def test_energy_consumption(self):
        percentage = data.energy_percentage(total_energy=500, days=10)
        self.assertEqual(percentage, 10)
