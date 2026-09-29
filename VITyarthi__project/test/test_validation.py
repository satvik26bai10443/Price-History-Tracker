import unittest
from tracker import validation as v


class ValidationTests(unittest.TestCase):
    def test_parse_price_formats(self):
        self.assertEqual(v.parse_price("65,125"), 65125)
        self.assertEqual(v.parse_price("\u20b970000"), 70000)

    def test_parse_price_rejects_bad_input(self):
        for bad in ("", "abc", "-5", "0", "12.5"):
            with self.assertRaises(ValueError):
                v.parse_price(bad)

    def test_parse_date(self):
        self.assertEqual(v.parse_date("2026-09-17"), "2026-09-17")
        with self.assertRaises(ValueError):
            v.parse_date("17/09/2026")

    def test_parse_choice(self):
        self.assertEqual(v.parse_choice(" 2 ", 3), 2)
        for bad in ("0", "4", "x", ""):
            with self.assertRaises(ValueError):
                v.parse_choice(bad, 3)

    def test_find_outliers_flags_typo(self):
        self.assertEqual(v.find_outliers([62000, 63000, 6487, 64000, 65000]), [2])
        self.assertEqual(v.find_outliers([100, 101, 102]), [])


if __name__ == "__main__":
    unittest.main()