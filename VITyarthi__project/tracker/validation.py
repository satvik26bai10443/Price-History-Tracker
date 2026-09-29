from datetime import datetime
from statistics import median

from .config import OUTLIER_TOLERANCE


def parse_choice(text, count):
    text = text.strip()
    if not text.isdigit() or not 1 <= int(text) <= count:
        raise ValueError(f"Please enter a number between 1 and {count}.")
    return int(text)


def parse_price(text):
    cleaned = text.strip().replace(",", "").replace("\u20b9", "")
    if not cleaned.isdigit() or int(cleaned) <= 0:
        raise ValueError("Price must be a positive whole number.")
    return int(cleaned)


def parse_date(text):
    try:
        return datetime.strptime(text.strip(), "%Y-%m-%d").date().isoformat()
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format, e.g. 2026-09-17.")


def parse_name(text):
    name = text.strip()
    if not name:
        raise ValueError("Name cannot be empty.")
    return name


def find_outliers(prices, tolerance=OUTLIER_TOLERANCE):
    if not prices:
        return []
    mid = median(prices)
    return [i for i, p in enumerate(prices) if abs(p - mid) / mid > tolerance]