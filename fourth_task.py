# Add Suffix
# Objective: Write a function `add_suffix` that returns a lambda expression. This lambda expression
# should transform its input by adding a specified suffix at the end.
# Parameters:
# - suffix: A string representing the suffix to be added to the input.
# Returns:
# - A lambda function that takes a string input and appends the specified suffix to it.

def add_suffix(suffix):
    return lambda word: word + suffix



# Examples:
add_able = add_suffix("able")
print(add_able("remark"))  # Expected: "remarkable"
print(add_able("break"))   # Expected: "breakable"

add_ment = add_suffix("ment")
print(add_ment("enjoy"))   # Expected: "enjoyment"
print(add_ment("develop")) # Expected: "development"