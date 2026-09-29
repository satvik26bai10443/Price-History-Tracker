from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "prices.json"
LOG_FILE = BASE_DIR / "logs" / "tracker.log"

CURRENCY = "\u20b9"          # Indian rupee sign
OUTLIER_TOLERANCE = 0.5      # price >50% away from the median is flagged
TREND_WINDOW = 4             # weeks compared when judging the trend
TREND_THRESHOLD = 0.01       # <1% change counts as "Stable"
BAR_WIDTH = 40               # width of the text bar chart