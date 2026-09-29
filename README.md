Price History Tracker
Overview
A Python command-line application that tracks the weekly prices of phones, laptops and headphones (in ₹), analyses the history, and advises whether the current price is a good time to buy. See statement.md for the full problem statement.
Features
Data management (CRUD): add, update and delete price records and add new products; data saved to data/prices.json.
Analytics: Best Price (median), Highest Price, Must Buy Price (minimum), average, mode, percentage change, trend (Rising / Falling / Stable) and a BUY / FAIR / WAIT recommendation.
Comparison: rank the products in a category by price change.
Visualization: weekly text bar chart and an optional line graph (date on X-axis, price on Y-axis).
Reliability: input validation, outlier warnings (e.g. a price far from the median), atomic file saves, and logging to logs/tracker.log.
Technologies Used
Python 3.8+, standard library (json, statistics, logging, unittest), optional matplotlib for the line graph, Git/GitHub.
Project Structure
price_tracker/
├── main.py                 # entry point
├── tracker/
│   ├── config.py           # constants and file paths
│   ├── logger.py           # logging setup
│   ├── validation.py       # input checks and outlier detection
│   ├── storage.py          # Module 1: JSON storage + CRUD
│   ├── analytics.py        # Module 2: statistics, trend, advice
│   ├── display.py          # Module 3: tables, bar chart, line graph
│   └── menu.py             # menus and workflow
├── tests/                  # unit tests
├── data/prices.json        # price history
├── statement.md
├── requirements.txt
└── README.md
Installation and Running
git clone <your-repo-url>
cd price_tracker
pip install -r requirements.txt     # only needed for the line graph
python main.py
In Google Colab, upload the folder and run !python main.py.
Testing
python -m unittest discover -v
17 tests cover validation, storage (CRUD, corrupt or missing files) and analytics.
Sample Output
iPhone 15 - price summary
  Best Price (median) : ₹69,345
  Highest Price       : ₹74,678  (2026-09-10)
  Must Buy Price (min): ₹65,125  (2026-03-26)
  Average Price       : ₹69,673
  Most Common (mode)  : No repeated price
  Change since start  : +14.7%  over 25 weeks
  Trend               : Rising
  Advice              : WAIT - latest price is more than 5% above the typical price.

2026-03-26     ₹65,125  #
2026-05-14     ₹69,134  #################
2026-09-10     ₹74,678  ########################################
