from statistics import mean, median, multimode

from .config import TREND_THRESHOLD, TREND_WINDOW


def summarize(records):
    
    if not records:
        raise ValueError("No price data available.")
    prices = [r["price"] for r in records]
    hi, lo = max(prices), min(prices)
    modes = multimode(prices)
    return {
        "best_price": median(prices),           
        "highest_price": hi,
        "highest_date": records[prices.index(hi)]["date"],
        "must_buy_price": lo,                       
        "must_buy_date": records[prices.index(lo)]["date"],
        "average": mean(prices),
        "mode": None if len(modes) == len(set(prices)) else modes[0],
        "first": prices[0],
        "latest": prices[-1],
        "change_pct": (prices[-1] - prices[0]) / prices[0] * 100,
        "weeks": len(prices),
    }


def trend(records, window=TREND_WINDOW):
    prices = [r["price"] for r in records]
    if len(prices) < 2 * window:
        return "Not enough data"
    recent = mean(prices[-window:])
    earlier = mean(prices[-2 * window:-window])
    change = (recent - earlier) / earlier
    if change > TREND_THRESHOLD:
        return "Rising"
    if change < -TREND_THRESHOLD:
        return "Falling"
    return "Stable"


def recommendation(records):
    s = summarize(records)
    latest, typical = s["latest"], s["best_price"]
    if latest <= typical:
        return "BUY NOW - latest price is at or below the typical (median) price."
    if latest <= typical * 1.05:
        return "FAIR - latest price is within 5% of the typical price."
    return "WAIT - latest price is more than 5% above the typical price."


def compare_products(products):
    rows = []
    for name, records in products.items():
        if records:
            s = summarize(records)
            rows.append((name, s["latest"], s["best_price"], s["change_pct"]))
    return sorted(rows, key=lambda r: r[3], reverse=True)