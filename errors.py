class InvalidDate(ValueError):
    def __init__(self, message):
        super().__init__(message)

    
class InvalidCountry(ValueError):
    def __init__(self, message):
        super().__init__(message)