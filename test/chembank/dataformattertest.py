from unittest import TestCase
from chembank import DataFormatter

class DataFormatterTest(TestCase):

    def test_print(self):
        df = DataFormatter([])
        self.assertEqual("no variables", df.prn("no variables", test=True))
        self.assertEqual("fooConc. Sulfuric Acidbar", df.prn("foo{{chemical.sulfuricacid98}}bar", test=True))
        self.assertEqual("foo{{chemical.invalid}}bar", df.prn("foo{{chemical.invalid}}bar", test=True))

        self.assertEqual(
                "37% Sulfuric AcidConc. Sulfuric Acid",
                df.prn("{{chemical.sulfuricacid37}}{{chemical.sulfuricacid98}}", test=True))
