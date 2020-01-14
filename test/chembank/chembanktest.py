from unittest import TestCase
from chembank import ChemBank

class ChemBankTest(TestCase):

    def setUp(self):
        self.cb = ChemBank("test/data")

    def test_list_experiments(self):
        self.assertEqual(
            ["dac1cab6-eee3-4903-8a1a-ea33ad744528"],
            [ item['identifier'] for item in self.cb.list_experiments() ]
        )

    def test_search_experiments(self):
        print (self.cb.list_experiments())
