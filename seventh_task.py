
# Objective: Create a class `AgeError` as a custom exception and a function `check_age` that raises `AgeError` if age is below 18 or above 120.
# Parameters:
# - age: An integer representing a person's age.
# Returns:
# - True if the age is valid, otherwise raises `AgeError`.
# Details:
# - `AgeError` should extend from `Exception` and include an error message that indicates the invalid age range.

class AgeError():
    pass

def check_age(age):
    if not 18 <= age <= 120:
        pass
    return True

# Examples:
# print(check_age(25))  # Expected: True
# print(check_age(17))  # Expected to raise: AgeError: Invalid age: 17. Age must be between 18 and 120
# print(check_age(121)) # Expected to raise: AgeError: Invalid age: 121. Age must be between 18 and 120


class AgeError(Exception):
    def __init__(self, age):
        self.message = f"Invalid age: {age}. Age must be between 18 and 120."
        super().__init__(self.message)

# Define the function to check age
def check_age(age):
    if not 18 <= age <= 120:
        raise AgeError(age)
    return True

# Examples:
print(check_age(25))  # Expected: True
try:
    print(check_age(17))  # Expected to raise: AgeError: Invalid age: 17. Age must be between 18 and 120
except AgeError as e:
    print(e)

try:
    print(check_age(121)) # Expected to raise: AgeError: Invalid age: 121. Age must be between 18 and 120
except AgeError as e:
    print(e)

# Output:
# True

