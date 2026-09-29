Problem Statement
Problem
Prices of electronics such as phones, laptops and headphones change from week to week. Shoppers usually see only today's price, so they cannot tell whether it is a good deal, a temporary spike, or part of a long-term rise. Price history is scattered across shops and is hard to compare.
Proposed Solution
Price History Tracker is a Python command-line application that stores weekly prices for products, analyses them, and tells the user whether the current price is a good time to buy.
Scope
In scope
Weekly price history for phones, laptops and headphones (9 sample products, 25 weeks each)
Storing prices in a JSON file, with add / update / delete operations
Statistics: median ("Best Price"), highest, lowest ("Must Buy Price"), average, mode, percentage change
Trend detection (Rising / Falling / Stable) and a simple buy / fair / wait recommendation
Comparing products within a category
Text bar chart and an optional line graph (date vs price)
Input validation, error handling, logging and unit tests
Out of scope
Fetching live prices from shopping websites
User accounts, a web or mobile interface, price-drop notifications
Target Users
Students and general shoppers deciding when to buy a gadget
Anyone who wants a quick, offline way to review price trends
Learners studying Python data handling, modular design and testing
High-Level Features
Data Management module: store, add, update and delete price records safely (JSON).
Analytics module: summary statistics, trend detection, buy recommendation, product comparison.
Visualization module: formatted summary, weekly bar chart and line graph.
Input validation, outlier warnings for suspicious prices, and activity logging.
# Core program uses only the Python standard library.
# Optional - only needed for the line graph:
matplotlib

