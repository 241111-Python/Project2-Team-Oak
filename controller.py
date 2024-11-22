import sys

def handle_user_input(user_selection: str):
    match user_selection:
        case "x":
            exit_game()
        case "e":
            handle_examine_entry()
        case "f":
            handle_filter_data()
        case "s":
            handle_sort_data()

def exit_game():
    sys.exit(0)

def handle_examine_entry():
    print("Examining an individual entry...")

def handle_filter_data():
    print("Filtering data...")

def handle_sort_data():
    print("Sorting data...")