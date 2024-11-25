import sys
import csv
import view
import Reader
from Model import Model

# TODO: this might not belong here.
burgerData = Reader.read_big_mac()
model = Model(burgerData)

def handle_user_input(userSelection: str):
    match userSelection:
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
        case "c":
            handle_print_countries()
        case "g":
            handle_graph_data()
        case "d":
            handle_print_dates()

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

    # ask for the entry the user wants
    # TODO: The data is sparsely populated, so an arbitrary date is not going to work. 
    print("Enter a date (yyyy-mm-dd) and country, separated by a comma: ")
    try:
        date, country = input().split(",")
        country = country.strip()
        burgers = model.get_burger_by_date_and_country(date, country)
        if not burgers:
            print(f"No data found for {country} on {date}")
        for burger in burgers:
            print(burger)
    except Exception as e:
        print("An error occured in validating the data:", e)

def handle_filter_data():
    print("Filtering data...")
    #1. filter as much as you want
    #2. sort by 1 parameter
    #2. filter the data by date, and choose how to sort(Name, local_price,dollar_ex,dollar_price)
    try:
        burgers = burgerData
        filterCondition = True
        while filterCondition != False:
            filterCondition = input("How do you want to filter burgers? (date, code, country, localPrice, exchangeRate, USD) - type 'f' to stop filtering: ")
            if filterCondition != 'f':
                value = input("What is the value you want to look for?: ")
                burgers = model.get_burger_by_attr(burgers, filterCondition, value)
            else:
                break
        
        sortCondition = input("How do you want to sort data? - type 'f' to stop sorting: ")
        if sortCondition != 'f':
            sortedBurgers = model.sort_burgers_by_attr(burgers, sortCondition)
        else:
            sortedBurgers = burgers
        model.print_burgers(sortedBurgers)
    except Exception as e:
        print("An error occured in validating the data:", e)

def handle_sort_data():
    print("Sorting data...")

def handle_print_countries():
    view.display_countries(model.get_countries())

def handle_graph_data():
    c1 = input("Would you like to see the change in USD price over time or the exchange rate over time?\n(USD/Rate): ").lower()
    while (c1 not in ['usd','rate']):
        print("Invalid input")
        c1 = input("Would you like to see the change in USD price over time or the exchange rate over time?\n(USD/Rate): ").lower()    
    
    c2 = input("Which Country would you like to graph? ")

    while not model.validate_country(c2):
        c2 = input("Which Country would you like to graph? ")
    
    if c1 == 'usd':
        view.graph_usd_year_by_country(burgerData, c2)
    elif c1 == 'rate':
        view.graph_exchange_year_by_country(burgerData, c2)

def handle_print_dates():
    view.display_dates(model.get_dates())