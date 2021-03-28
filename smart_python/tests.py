# in-built
import unittest
# created file
from new_api import get_rates
from new_api import output_to_csv


class TestRates(unittest.TestCase):

    def test_sum(self):
        self.assertDictEqual(d1=get_rates(), d2=get_rates())

    def test_csv(self):
        self.assertIsNotNone(output_to_csv())


if __name__ == '__main__':
    unittest.main()
    print("Tests have passed")
