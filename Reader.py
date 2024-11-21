import csv
from burger import Burger
bigMac = "bigmac.csv"

# reads the data and returns a list of Burger objects
def readBigMac(data=bigMac):

    # reads through the data file and places each row into a sub list,
    # then each sub list is placed into the burgerList
    burgerList = []
    burgerObj = []
    with open (data, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            burgerList.append(row)

        # removes the data legend
        burgerList.pop(0)

    # creates a Burger object from each sub list and adds it to the burgerObj list
    for row in burgerList:
        brg = Burger()
        brg.date = row[0]
        brg.code = row[1]
        brg.country = row[2]
        brg.localPrice = row[3]
        brg.exchangeRate = row[4]
        brg.USD = row[5]
        burgerObj.append(brg)

    return burgerObj

def getCountries(data=bigMac) -> set:
    lst = readBigMac(data)
    countries = set()
    for brg in lst:
        countries.add(brg.country)
    return countries

def displayCountries(data=bigMac):
    st = list(getCountries(data))
    st.sort()
    row = []
    for i in st:
        if len(row) < 3:
            row.append(i)
        else:
            row.append(i)
            print(f'{row[0]:21}{row[1]:21}{row[2]:21}{row[3]:21}')
            row.clear()
    # if the number of our countries isn't divisible by 4, this prints out the leftovers
    for i in row:
        print(f'{i:21}', end="")
