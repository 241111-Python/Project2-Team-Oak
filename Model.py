from collections import defaultdict
from errors import InvalidCountry, InvalidDate
import statistics as stats
import re
import Reader as r
class Model:
    def __init__(self, data=None):
        self.data = data

    # Here is where you would put any sorting methods, filtering methods, etc on the data. 

    def print_burgers(self, burgers):
        for burger in burgers:
            print(burger)

    def sort_burgers_by_attr(self, burgers, attr):
        return sorted(burgers, key=lambda burgers: getattr(burgers, attr))
    
    def get_burger_by_date_and_country(self, date, country):
        self.validate_date(date)
        self.validate_country(country)
        return [burger for burger in self.data if burger.date == date and burger.country == country]   
    
    def get_burger_by_attr(self, burgers, attr, value):
        return [burger for burger in burgers if getattr(burger, attr) == value]
        
    def get_countries(self) -> set:
        countries = set()
        for brg in self.data:
            countries.add(brg.country)
        return sorted(list(countries))
    
    def get_dates(self):
        dates = set()
        for brg in self.data:
            dates.add(brg.date)
        return sorted(list(dates))
     
    def validate_date(self, date):
        print("Validating date...")
        if not re.fullmatch(r"^\d{4}-\d{2}-\d{2}$", date):
            raise InvalidDate(f"{date} is not correctly formatted. Please use yyyy-mm-dd.")
        return True

    def validate_country(self, country):
        country = country.title()
        # if not re.fullmatch(r"^[A-Z][a-z]+(?: [A-Z][a-z]+)*$", country):
        if country in self.get_countries():
            return True
        else:
            raise InvalidCountry(f"{country} is not correctly formatted, or is not a string.")
            return False

    def get_mean_usd_by_date(self, date):
        lst = []
        for i in self.data:
            if i.date == date:
                lst.append(i.USD)
        return stats.mean(lst)
    
    def get_median_usd_by_year(self, year):
        lst = []
        for i in self.data:
            if i.date[:4] == year:
                lst.append(i.USD)
        return stats.median(lst)
    
    def get_max_usd_by_year(self, year):
        lst = []
        for i in self.data:
            if i.date[:4] == year:
                lst.append(i.USD)
        return max(lst)

    def get_min_usd_by_year(self, year):
        lst = []
        for i in self.data:
            if i.date[:4] == year:
                lst.append(i.USD)
        return min(lst) 

    def get_stdev_usd_by_year(self, year):
        lst = []
        for i in self.data:
            if i.date[:4] == year:
                lst.append(i.USD)
        return stats.stdev(lst)  
    
    def get_range_usd_by_year(self, year):
        lst = []
        for i in self.data:
            if i.date[:4] == year:
                lst.append(i.USD)
        return max(lst) - min(lst) 
    
    def get_mean_usd_by_country(self, country):
        lst = []
        for i in self.data:
            if i.country == country:
                lst.append(i.USD)
        return stats.mean(lst)
    
    def get_median_usd_by_country(self, country):
        lst = []
        for i in self.data:
            if i.country == country:
                lst.append(i.USD)
        return stats.median(lst)
    
    def get_max_usd_by_country(self, country):
        lst = []
        for i in self.data:
            if i.country == country:
                lst.append(i.USD)
        return max(lst)

    def get_min_usd_by_country(self, country):
        lst = []
        for i in self.data:
            if i.country == country:
                lst.append(i.USD)
        return min(lst) 

    def get_stdev_usd_by_country(self, country):
        lst = []
        for i in self.data:
            if i.country == country:
                lst.append(i.USD)
        return stats.stdev(lst)  
    
    def get_range_usd_by_country(self, country):
        lst = []
        for i in self.data:
            if i.country == country:
                lst.append(i.USD)
        return max(lst) - min(lst) 

    # This returns a list of (country, ppp) Tuples.
    # It defaults to using the US as a metric, but a different country can be used in its place
    def ppp_date_report(self, date, relativeCountry="United States"):
        lst=[]
        ppp = []
        delta = 1
        for i in self.data:
            if i.date == date:
                lst.append(i)
                if i.country == relativeCountry:
                    delta = i.USD
        for i in lst:
            ppp.append((i.country, delta/i.USD))
        return ppp

    # Similar to the above function, but the return is a list of (date, ppp) tuples    
    def ppp_country_report(self, country, relativeCountry="United States"):
        lst = []
        rel = []
        ppp = []
        for i in self.data:
            if i.country == country:
                lst.append(i)
            if i.country == relativeCountry:
                rel.append(i)
        for i in lst:
            for x in rel:
                if i.date == x.date:
                    ppp.append((i.date, x.USD/i.USD))
        return ppp
    
    def get_standard_report_statistics(self):
        dates = self.get_dates()
        names = ["Date", "Mean", "Median", "Standard Deviation", "Min", "Max"]
        reportStatistics = defaultdict(list)
        burgerData = self.sort_burgers_by_attr(self.data, "date")
        currentDate = burgerData[0].date
        currentUSD = []
        for i, burger in enumerate(burgerData):
            if burger.date != currentDate or i == len(burgerData) - 1:
                # Process current burger data and save it in data
                reportStatistics["Mean"].append(str(stats.mean(currentUSD)))
                reportStatistics["Median"].append(str(stats.median(currentUSD)))
                reportStatistics["Standard Deviation"].append(str(stats.stdev(currentUSD)))
                reportStatistics["Min"].append(str(min(currentUSD)))
                reportStatistics["Max"].append(str(max(currentUSD)))
                currentUSD = []
                currentDate = burger.date
            else:
                currentUSD.append(burger.USD)

        return names, reportStatistics
        # print(report.generate_report(names, zip(dates, means, medians), [15, 20, 15]))

