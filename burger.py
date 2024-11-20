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

