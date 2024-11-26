import csv
from burger import Burger
bigMac = "bigmac.csv"

# TODO: We should probably turn our list of burgers into a class
# so that they aren't being read in over and over.

# reads the data and returns a list of Burger objects
def read_big_mac(data=bigMac):

    # reads through the data file and places each row into a sub list,
    # then each sub list is placed into the burgerList
    burgerList = []
    burgerObj = []
    try:
        with open (data) as file:
            reader = csv.reader(file)
            for row in reader:
                burgerList.append(row)

            # removes the data legend
            burgerList.pop(0)

        # creates a Burger object from each sub list and adds it to the burgerObj list
        for row in burgerList:
            brg = Burger(row[0], row[1], row[2], row[3], row[4], row[5])
            burgerObj.append(brg)
        return burgerObj
    except FileNotFoundError as e:
        print(f"Could not locate {bigMac}", e)


def get_burger_by_date_and_country(date, country):
    burgers = read_big_mac(data=bigMac)
    return [burger for burger in burgers if burger.date == date and burger.country == country]