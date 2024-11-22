import csv
from burger import Burger
bigMac = "bigmac.csv"

# reads the data and returns a list of Burger objects
def readBigMac(data=bigMac):

    # reads through the data file and places each row into a sub list,
    # then each sub list is placed into the burgerList
    burgerList = []
    burgerObj = []
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

def getCountries(data=bigMac) -> set:
    lst = readBigMac(data)
    countries = set()
    for brg in lst:
        countries.add(brg.country)
    return countries
