class Model:
    def __init__(self, data=None):
        self.data = data

    # Here is where you would put any sorting methods, filtering methods, etc on the data. 
    def get_burger_by_date_and_country(self, date, country):
        return [burger for burger in self.data if burger.date == date and burger.country == country]
    
    def validate_date(date):
        print("Validating date...")
        return True

    def validate_country(country):
        print("Validating country...")
        return True
