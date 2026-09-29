"""Entry point: python main.py"""
from tracker import menu, storage
from tracker.logger import get_logger

log = get_logger("main")


def main():
    try:
        data = storage.load_data()
    except storage.StorageError as exc:
        print(f"Cannot start: {exc}")
        return
    log.info("Application started")
    try:
        menu.run(data)
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")
    log.info("Application closed")


if __name__ == "__main__":
    main()