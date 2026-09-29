import unittest
from tracker import analytics as a


def recs(prices):
    return [{"date": f"2026-01-{i + 1:02d}", "price": p} for i, p in enumerate(prices)]


class AnalyticsTests(unittest.TestCase):
    def test_summary_values(self):
        s = a.summarize(recs([100, 200, 300, 400, 500]))
        self.assertEqual(s["best_price"], 300)
        self.assertEqual(s["highest_price"], 500)
        self.assertEqual(s["must_buy_price"], 100)
        self.assertEqual(s["change_pct"], 400)
        self.assertIsNone(s["mode"])

    def test_mode_when_price_repeats(self):
        self.assertEqual(a.summarize(recs([100, 200, 200, 300]))["mode"], 200)

    def test_empty_data_raises(self):
        with self.assertRaises(ValueError):
            a.summarize([])

    def test_trend(self):
        self.assertEqual(a.trend(recs(list(range(100, 116)))), "Rising")
        self.assertEqual(a.trend(recs(list(range(116, 100, -1)))), "Falling")
        self.assertEqual(a.trend(recs([100] * 16)), "Stable")
        self.assertEqual(a.trend(recs([100, 101])), "Not enough data")

    def test_recommendation(self):
        self.assertTrue(a.recommendation(recs([100, 200, 90])).startswith("BUY"))
        self.assertTrue(a.recommendation(recs([100, 100, 100, 200])).startswith("WAIT"))

    def test_compare_sorted_by_change(self):
        rows = a.compare_products({"A": recs([100, 110]), "B": recs([100, 150])})
        self.assertEqual([r[0] for r in rows], ["B", "A"])


if __name__ == "__main__":
    unittest.main()