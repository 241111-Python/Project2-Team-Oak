import sys
import csv
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
        case "u":
            handle_upload_data()

def exit_game():
    sys.exit(0)

def handle_upload_data():
    dataPath = input("upload your file (csv only): ")
    if dataPath[-4:] == ".csv":
        with open(dataPath, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for i, row in enumerate(reader):
                if i < 5:
                    print(row)
    else:
        print("only csv allowed now")

def handle_examine_entry():
    print("Examining an individual entry...")

def handle_filter_data():
    print("Filtering data...")

def handle_sort_data():
    print("Sorting data...")