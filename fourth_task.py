# Encapsulate Vehicle Class
# Objective: Create a class `Vehicle` with private attributes for `make`, `model`, and `year`, and implement getters and setters for each.
# Parameters:
# - make: String
# - model: String
# - year: Integer
# Returns:
# - None directly; use properties to get/set values.
# Details:
# - Use property decorators to create getters and setters.
# - Ensure invalid values (e.g., non-string for make/model, non-integer/year before 1886) raise ValueError.

class Vehicle:
	pass

# Desired Outcome:
# v = Vehicle()
# v.make = "Toyota"
# v.model = "Corolla"
# v.year = 2005
# print(v.make, v.model, v.year)  # Expected: Toyota Corolla 2005
# v.year = 1800  # Should raise ValueError: Invalid year

class Vehicle:
    def __init__(self):
        self.__make = None
        self.__model = None
        self.__year = None

    @property
    def make(self):
        return self.__make

    @make.setter # setter method for make. setter is using the make property like a function. without this, make property will be read-only now it is read-write
    def make(self, value):
        if not isinstance(value, str):
            raise ValueError("Invalid make")
        self.__make = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not isinstance(value, str):
            raise ValueError("Invalid model")
        self.__model = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if not isinstance(value, int) or value < 1886:
            raise ValueError("Invalid year")
        self.__year = value

v = Vehicle()
v.make = "Toyota"
v.model = "Corolla"
v.year = 2005
print(v.make, v.model, v.year)