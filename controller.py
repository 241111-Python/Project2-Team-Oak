import sys
import view
import util
import Reader

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

    # ask for the entry the user wants
    # TODO: The data is sparsely populated, so an arbitrary date is not going to work. 
    print("Enter a date (yyyy-mm-dd) and country, separated by a comma: ")
    date, country = input().split(",")

    # Validate user inputs
    util.validate_date(date)
    util.validate_country(country)

    burgers = Reader.get_burger_by_date_and_country(date, country)
    for burger in burgers:
        print(burger)

def handle_filter_data():
    print("Filtering data...")

def handle_sort_data():
    print("Sorting data...")