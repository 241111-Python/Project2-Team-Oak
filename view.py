import matplotlib.pyplot as plt
from burger import Burger
menuOptions = {
    "Quit": "x",
    "Examine an entry": "e", 
    "Filter on an feature": "f",
    "Sort on a feature": "s",
    "Upload data(csv only)": "u",
    "Print countries": "c",
    "Graph data by country": "g",
    "Print dates": "d"
}

def print_menu_options():
    for option, command in menuOptions.items():
        print(f"{option:.<30}{command}")

def display_countries(countrySet):
    columnar_printer(countrySet, numRows=4)

def columnar_printer(data, numRows=1):
    width = 80
    columnWidth = width // numRows

    if numRows == 1:
        columnWidth = None

    def formatDatum(datum):
        # Check to see if length is at least columnWidth, otherwise left justify and pad
        return f"{str(datum)[:columnWidth]:<{columnWidth}}"
    
    row = []
    for i in data:
        if len(row) < numRows - 1:
            row.append(i)
        else:
            row.append(i)
            # print(row[0])
            result = [formatDatum(d) for d in row]
            # print(f'{row[0]:columnWidth}{row[1]:columnWidth}{row[2]:columnWidth}{row[3]:columnWidth}')
            print(" ".join(result))
            row.clear()
    # if the number of our countries isn't divisible by numRows, this prints out the leftovers
    for i in row:
        result = [formatDatum(d) for d in row]
        print(" ".join(result))

def graph_usd_year_by_country(data, country):
    x = []
    y = []
    for i in data:
        if i.country == country:
            x.append(i.date_as_float())
            y.append(i.USD)
    plt.plot(x,y)
    plt.xlabel("Year")
    plt.ylabel("USD")
    plt.title(country)
    plt.savefig(f'./graphs/usd_{country}.png')
    plt.show()

def graph_exchange_year_by_country(data, country):
    x = []
    y = []
    for i in data:
        if i.country == country:
            x.append(i.date_as_float())
            y.append(i.exchangeRate)
    plt.plot(x,y)
    plt.xlabel("Year")
    plt.ylabel("Exchange Rate")
    plt.title(country)
    plt.savefig(f'./graphs/exchange_{country}.png')
    plt.show()

#def graph_ppp_year_by_country(data, country):
#    x = []
#    y = []
#    for i in data:
#        if i.country == country:
#            x.append(i.date_as_float())
#            y.append()
#    plt.plot(x,y)
#    plt.xlabel("Year")
#    plt.ylabel("Purchasing Power Parity")
#    plt.title(country)
#    plt.savefig(f'./graphs/ppp_{country}.png')
#    plt.show()    

def display_dates(dateSet):
    columnar_printer(dateSet, numRows=4)
