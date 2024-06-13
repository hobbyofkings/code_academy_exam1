# Class: Country
# Objective: Enhance the `Country` class to include an attribute `is_big` and a method to compare population density with another country.
# Details:
# - The `is_big` attribute should be set to True if either of the following criteria are met:
#   - The population is greater than 250 million.
#   - The area is larger than 3 million square km.
# - The class should also include a method `compare_pd` that compares the population density of the country with another country object.
# - The `compare_pd` method should return a string in the following format: "{country} has a {smaller / larger} population density than {other_country}".
# - Population density is calculated as the population divided by the area.

class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = self.population > 250000000 or self.area > 3000000

    def compare_pd(self, country):
        pd = self.population / self.area
        other_pd = country.population / country.area
        if pd > other_pd:
            return f"{self.name} has a larger population density than {country.name}"
        elif pd < other_pd:
            return f"{self.name} has a smaller population density than {country.name}"
        else:
            return f"{self.name} has the same population density as {country.name}"


# Examples:
australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

print(australia.is_big)  # Expected: True
print(andorra.is_big)  # Expected: False
print(andorra.compare_pd(australia))  # Expected: "Andorra has a larger population density than Australia"