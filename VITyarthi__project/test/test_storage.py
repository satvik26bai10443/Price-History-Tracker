import os
import tempfile
import unittest

from tracker import storage as s


class StorageTests(unittest.TestCase):
    def setUp(self):
        self.data = {"Phones": {"X": [{"date": "2026-01-01", "price": 100}]}}

    def test_add_keeps_dates_sorted(self):
        s.add_record(self.data, "Phones", "X", "2025-12-25", 90)
        self.assertEqual(self.data["Phones"]["X"][0]["date"], "2025-12-25")

    def test_duplicate_date_rejected(self):
        with self.assertRaises(s.StorageError):
            s.add_record(self.data, "Phones", "X", "2026-01-01", 95)

    def test_update_and_delete(self):
        s.update_record(self.data, "Phones", "X", "2026-01-01", 120)
        self.assertEqual(self.data["Phones"]["X"][0]["price"], 120)
        s.delete_record(self.data, "Phones", "X", "2026-01-01")
        self.assertEqual(self.data["Phones"]["X"], [])

    def test_unknown_product_and_missing_date(self):
        with self.assertRaises(s.StorageError):
            s.add_record(self.data, "Phones", "Nope", "2026-02-01", 1)
        with self.assertRaises(s.StorageError):
            s.delete_record(self.data, "Phones", "X", "2030-01-01")

    def test_save_and_load_round_trip(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "p.json")
            s.save_data(self.data, path)
            self.assertEqual(s.load_data(path), self.data)

    def test_missing_and_corrupt_file(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(s.StorageError):
                s.load_data(os.path.join(d, "none.json"))
            bad = os.path.join(d, "bad.json")
            with open(bad, "w") as f:
                f.write("{oops")
            with self.assertRaises(s.StorageError):
                s.load_data(bad)


if __name__ == "__main__":
    unittest.main()