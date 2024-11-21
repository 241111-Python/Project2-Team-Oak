class Burger:
    # Constructor
    def __init__(self, date, code, country, localPrice, exchangeRate, USD):
        self.date = date
        self.code = code
        self.country = country
        self.localPrice = localPrice
        self.exchangeRate = exchangeRate
        self.USD = USD
    
    def __str__(self):
        return f'[{self.date} -- {self.code} -- {self.country} -- {self.localPrice} -- {self.exchangeRate} -- {self.USD}]'
    
    def info(self):
        return str(f"Date: {self.date}\nCurrency Code: {self.code}\nCountry: {self.country}\nLocal Prince: {self.localPrice}\nExchange Rate: {self.exchangeRate}\nDollar Price: ${self.USD}")
