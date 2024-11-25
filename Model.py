from errors import InvalidCountry, InvalidDate
import re
import Reader as r
class Model:
    def __init__(self, data=None):
        self.data = data

    # Here is where you would put any sorting methods, filtering methods, etc on the data. 
    def get_burger_by_date_and_country(self, date, country):
        self.validate_date(date)
        self.validate_country(country)
        return [burger for burger in self.data if burger.date == date and burger.country == country]   
        
    def get_countries(self) -> set:
        countries = set()
        lst = []
        for brg in self.data:
            countries.add(brg.country)
        for i in countries:
            lst.append(i)
        return sorted(lst)
    
    def get_dates(self):
        dates = set()
        for brg in self.data:
            dates.add(brg.date)
        lst = []
        for i in dates:
            lst.append(i)
        return sorted(lst)
     
    def validate_date(self, date):
        print("Validating date...")
        if not re.fullmatch(r"^\d{4}-\d{2}-\d{2}$", date):
            raise InvalidDate(f"{date} is not correctly formatted. Please use yyyy-mm-dd.")
        return True

    def validate_country(self, country):
        print("Validating country...")
        if not re.fullmatch(r"^[A-Z][a-z]+$", country):
            raise InvalidCountry(f"{country} is not correctly formatted, or is not a string.")
        return True

if __name__ == "__main__":
    model = Model(r.read_big_mac())
    model.validate_country("Hong Kong")