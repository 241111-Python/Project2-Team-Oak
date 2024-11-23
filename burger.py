class Burger:
    # Constructor
    def __init__(self, date, code, country, localPrice, exchangeRate, USD):
        self.date = str(date)
        self.code = str(code)
        self.country = str(country)
        self.localPrice = float(localPrice)
        self.exchangeRate = float(exchangeRate)
        self.USD = float(USD)
    
    def __str__(self):
        return f'Date: {self.date} | Currency Code: {self.code} | Country: {self.country:20}| Local Price: {self.localPrice:<8.2f}| Exchange Rate: {self.exchangeRate:<8.2f} | USD: {self.USD:.2f}'

    def date_as_float(self):
        return (float(self.date[:4]) + (float(self.date[5:7])/12))
