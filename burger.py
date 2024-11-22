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
        return f'Date: {self.date} | Currency Code: {self.code} | Country: {self.country:20}| Local Price: {self.localPrice:<8.2f}| Exchange Rate: {self.exchangeRate:<8.2f} | USD: {self.USD:.2f}'
