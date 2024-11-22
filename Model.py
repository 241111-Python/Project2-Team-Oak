from errors import InvalidCountry, InvalidDate
import re
class Model:
    def __init__(self, data=None):
        self.data = data

    # Here is where you would put any sorting methods, filtering methods, etc on the data. 
    def get_burger_by_date_and_country(self, date, country):
        try:
            self.validate_date(date)
            self.validate_country(country)
            return [burger for burger in self.data if burger.date == date and burger.country == country]   
        except Exception as e:
            print("An error occured in validating the data:", e)
            return None

     
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
