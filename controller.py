import datetime
import sys
import csv
import view
import Reader
from Model import Model
from burger import Burger
import report
import logger

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
        case "u":
            handle_upload_data()
        case "c":
            handle_submenu_c()
        case "g":
            handle_submenu_g()
        case "r":
            handle_print_standard_report()
        case "ppp-d":
            handle_print_ppp_date_report()
        case "ppp-c":
            handle_print_ppp_country_report()

def exit_game():
    sys.exit(0)

def handle_upload_data(dataPath=None):
    global model
    global burgerData
    if not dataPath:
        dataPath = input("upload your file (csv only): ")
    if dataPath[-4:] == ".csv":
        burgerData = Reader.read_big_mac(data=dataPath)
        model = Model(burgerData)
    else:
        print("only csv allowed now")

def handle_generate_reports(report: str, additionalArgs: dict) -> None:
    result = ""
    fileName = ""
    if report == "standard":
        fileName="standard_report"
        result = handle_generate_standard_report()
    if report == "ppp":
        if (date := additionalArgs["date"]):
            fileName = f"ppp_{date}"
            result = handle_generate_ppp_date_report(date)
        if (country := additionalArgs["country"]):
            fileName = f"ppp_{country}"
            result = handle_generate_ppp_country_report(country)
    logger.export(result, fileName)

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

def handle_print_countries():
    view.display_countries(model.get_countries())

def handle_graph_data():
    while (c1 := input("Would you like to graph:\nUSD price over time \nExchange rate over time\nPPP over time\n(USD/Rate/PPP): ").lower()):
        if c1 not in ['usd','rate','ppp']:
            print("Invalid input")
        else:
            break
     
    countries = model.get_countries()
    while (c2 := input("Which Country would you like to graph? ")):
        if c2 not in countries:
            view.columnar_printer(countries, numRows=4)
            print("Please select a valid Country")
        else:
            break
    
    if c1 == 'usd':
        view.graph_usd_year_by_country(burgerData, c2)
    elif c1 == 'rate':
        view.graph_exchange_year_by_country(burgerData, c2)
    elif c1 == 'ppp':
        view.graph_ppp_year_by_country(model.ppp_country_report(c2), c2)

def handle_print_dates():
    view.display_dates(model.get_dates())

def handle_generate_standard_report():
    names, data = model.get_standard_report_statistics()
    dates = model.get_dates()

    # unpack and arrange data
    data = [data[name] for name in names[1:]]
    data = [dates] + data

    widths = [15] * len(names)
    return report.generate_report(names, zip(*data), widths)

def handle_print_standard_report():
    print(handle_generate_standard_report())

def handle_print_ppp_date_report():
    dates = model.get_dates()
    dates = [str(date) for date in dates]
    while (date := input("Enter a date for the report: ")):
        if date not in dates:
            print("Date not found. Here is a selection of dates:")
            view.columnar_printer(dates, numRows=4)
        else:
            break

    data = model.ppp_date_report(date)
    data = [(str(i), str(j)) for (i, j) in data]
    names = ["Country", "PPP"]
    widths = [25, 25]
    print(report.generate_report(names, data, widths))

def handle_print_ppp_country_report():
    countries = model.get_countries()
    while (country := input("Enter a country for the report: ")):
        if country not in countries:
            print("Country not found. Here is a selection of countries:")
            view.columnar_printer(countries, numRows=4)
        else:
            break

    data = model.ppp_country_report(country)
    data = [(str(i), str(j)) for (i, j) in data]
    names = ["Date", "PPP"]
    widths = [25, 25]
    print(report.generate_report(names, data, widths))

def handle_submenu_c():
    loop = True
    while(loop):
        choice = input("Would you like to print dates or countries? \n(d/c): ")
        if choice == 'c':
            handle_print_countries()
            loop = False
        elif choice == 'd':
            handle_print_dates()
            loop = False
        else:
            print("Invalid input\n")
    
def handle_submenu_g():
    while (choice := input("Would you like to view graphs or reports?\nPress x to exit.(g/r/x): ")):
        if choice == 'g':
            handle_graph_data()
        elif choice == 'r':
            while (pick := input("Would you like to view\nStandard Report\nCountry Report\nDate Report\nPress x to exit.(s/c/d/x): ")):
                if pick == 's':
                    handle_print_standard_report()
                elif pick == 'c':
                    handle_print_ppp_country_report()
                elif pick == 'd':
                    handle_print_ppp_date_report()
                elif pick == 'x':
                    break
                else:
                    print("Invalid Input\n")
        elif choice == 'x':            
            break
        else:
            print(f"Invalid selection: {choice}. Try again!")

def handle_generate_ppp_country_report(country: str) -> str:
    data = model.ppp_country_report(country)
    data = [(str(i), str(j)) for (i, j) in data]
    names = ["Date", "PPP"]
    widths = [25, 25]
    return report.generate_report(names, data, widths)

def handle_generate_ppp_date_report(date: str):
    data = model.ppp_date_report(date)
    data = [(str(i), str(j)) for (i, j) in data]
    names = ["Country", "PPP"]
    widths = [25, 25]
    return report.generate_report(names, data, widths)
