# Filter and Calculate Average Age of Adult Users
# Objective: Write a function `calculate_average_age_of_adults` that takes an array of user objects and returns
# the average age of all adult users as a numeric value. Only users who are 18 years or older are considered adults.
# Details:
# - The function should filter out users who are under 18 years old.
# - The function should compute the average of the 'age' values for the remaining adult user objects.
# - The result should be rounded to two decimal places if necessary.


# Example user data
users = [
    {"id": '1', "name": 'John Smith', "age": 20},
    {"id": '2', "name": 'Ann Smith', "age": 24},
    {"id": '3', "name": 'Tom Jones', "age": 31},
    {"id": '4', "name": 'Rose Peterson', "age": 17},
    {"id": '5', "name": 'Alex John', "age": 25},
    {"id": '6', "name": 'Ronald Jones', "age": 63},
    {"id": '7', "name": 'Elton Smith', "age": 16},
    {"id": '8', "name": 'Simon Peterson', "age": 30},
    {"id": '9', "name": 'Daniel Cane', "age": 51},
]

def calculate_average_age_of_adults(users):
    adult_users = list(filter(lambda user: user['age'] >= 18, users))
    average_age = sum([user['age'] for user in adult_users]) / len(adult_users)
    return round(average_age, 2)


# Testing the function
print(calculate_average_age_of_adults(users))  # This should print the average age of adult users (18+)