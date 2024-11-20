import csv
bigMac = "bigmac.csv"

class Burger:
    # Constructor
    def __int__(self, date, code, country, localPrice, exchangeRate, USD):
        self.date = date
        self.code = code
        self.country = country
        self.localPrice = localPrice
        self.exchangeRate = exchangeRate
        self.USD = USD
    
    def info(self):
        return str(f"Date: {self.date}\nCurrency Code: {self.code}\nCountry: {self.country}\nLocal Prince: {self.localPrice}\nExchange Rate: {self.exchangeRate}\nDollar Price: ${self.USD}")

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

        # returns a list of each Burger from our data set    
    return burgerObj
