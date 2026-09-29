"""User interaction: menus, prompts and the main workflow."""
from . import analytics, display, storage, validation
from .logger import get_logger

log = get_logger(__name__)


def ask(prompt, parser):
    """Keep asking until the parser accepts the input."""
    while True:
        try:
            return parser(input(prompt))
        except ValueError as exc:
            print(f"  ! {exc}")


def choose(title, options):
    print(f"\n{title}")
    for i, opt in enumerate(options, start=1):
        print(f"  {i}. {opt}")
    n = ask(f"Choose (1-{len(options)}): ", lambda t: validation.parse_choice(t, len(options)))
    return options[n - 1]


def pick_product(data):
    category = choose("Select a category:", list(data))
    if not data[category]:
        print("  No products in this category yet.")
        return category, None
    product = choose(f"{category}:", list(data[category]))
    return category, product


def view_analysis(data):
    category, product = pick_product(data)
    if product is None:
        return
    records = data[category][product]
    if not records:
        print("  No prices recorded for this product yet.")
        return
    display.print_summary(product, analytics.summarize(records))
    print(f"  Trend               : {analytics.trend(records)}")
    print(f"  Advice              : {analytics.recommendation(records)}")
    display.print_history(product, records)
    flagged = validation.find_outliers([r["price"] for r in records])
    for i in flagged:
        print(f"  ! Check {records[i]['date']}: {display.rupees(records[i]['price'])} "
              "looks unusual (possible typing mistake).")


def view_comparison(data):
    category = choose("Select a category to compare:", list(data))
    rows = analytics.compare_products(data[category])
    if rows:
        display.print_comparison(category, rows)
    else:
        print("  No data to compare.")


def show_graph(data):
    category, product = pick_product(data)
    if product and data[category][product]:
        display.show_line_chart(product, data[category][product])


def manage_data(data):
    action = choose("Manage data:", [
        "Add a price", "Update a price", "Delete a price", "Add a new product"])
    if action == "Add a new product":
        category = choose("Select a category:", list(data))
        name = ask("New product name: ", validation.parse_name)
        storage.add_product(data, category, name)
    else:
        category, product = pick_product(data)
        if product is None:
            return
        date = ask("Date (YYYY-MM-DD): ", validation.parse_date)
        if action == "Delete a price":
            storage.delete_record(data, category, product, date)
        else:
            price = ask("Price in rupees: ", validation.parse_price)
            if action == "Add a price":
                storage.add_record(data, category, product, date, price)
            else:
                storage.update_record(data, category, product, date, price)
    storage.save_data(data)
    print("  Saved.")


ACTIONS = {
    "View price analysis": view_analysis,
    "Compare products in a category": view_comparison,
    "Show line graph": show_graph,
    "Manage price data (add / update / delete)": manage_data,
}


def run(data):
    print("Price History Tracker")
    while True:
        choice = choose("Main menu:", list(ACTIONS) + ["Exit"])
        if choice == "Exit":
            print("Goodbye!")
            return
        try:
            ACTIONS[choice](data)
        except (storage.StorageError, ValueError) as exc:
            log.warning("Action failed: %s", exc)
            print(f"  ! {exc}")