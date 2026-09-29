from .config import BAR_WIDTH, CURRENCY


def rupees(amount):
    return f"{CURRENCY}{amount:,.0f}"


def print_summary(name, s):
    print(f"\n{name} - price summary")
    print(f"  Best Price (median) : {rupees(s['best_price'])}")
    print(f"  Highest Price       : {rupees(s['highest_price'])}  ({s['highest_date']})")
    print(f"  Must Buy Price (min): {rupees(s['must_buy_price'])}  ({s['must_buy_date']})")
    print(f"  Average Price       : {rupees(s['average'])}")
    mode = rupees(s["mode"]) if s["mode"] else "No repeated price"
    print(f"  Most Common (mode)  : {mode}")
    print(f"  Change since start  : {s['change_pct']:+.1f}%  over {s['weeks']} weeks")


def print_history(name, records):
    prices = [r["price"] for r in records]
    lo, hi = min(prices), max(prices)
    span = (hi - lo) or 1
    print(f"\n{name} - weekly price trend   (low {rupees(lo)} -> high {rupees(hi)})")
    print(f"{'Date':<12}{'Price':>10}  Trend")
    print("-" * (24 + BAR_WIDTH))
    for r in records:
        bar = "#" * max(1, round((r["price"] - lo) / span * BAR_WIDTH))
        print(f"{r['date']:<12}{rupees(r['price']):>10}  {bar}")


def print_comparison(category, rows):
    print(f"\n{category} - comparison (ranked by price change)")
    print(f"{'Product':<26}{'Latest':>10}{'Median':>10}{'Change':>9}")
    print("-" * 55)
    for name, latest, med, change in rows:
        print(f"{name:<26}{rupees(latest):>10}{rupees(med):>10}{change:>+8.1f}%")


def show_line_chart(name, records):
    """Line graph: Date on X-axis, Price on Y-axis (needs matplotlib)."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib is not installed. Run: pip install matplotlib")
        return
    dates = [r["date"] for r in records]
    prices = [r["price"] for r in records]
    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, marker="o")
    plt.title(f"{name} - Price History")
    plt.xlabel("Date")
    plt.ylabel(f"Price ({CURRENCY})")
    plt.xticks(dates[::3], rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()