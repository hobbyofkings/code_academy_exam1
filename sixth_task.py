# Make a Rug
# Objective: Write a function `make_rug` that accepts the height (m), width (n), and an optional character (proc),
# and generates a list with m elements. Each element is a string consisting of the given character repeated n times.
# If no character is given, the default character should be the hash symbol (#).
# Parameters:
# - m: An integer representing the height of the rug (number of elements in the list).
# - n: An integer representing the width of the rug (length of each string).
# - proc: An optional character used to fill the rug. The default is '#'.
# Returns:
# - A list of strings, each string consisting of the given character repeated n times.

def make_rug(m, n, proc='#'):
    return [proc * n for _ in range(m)]



# Examples:
print(make_rug(3, 5))       # Expected: ["#####", "#####", "#####"]
print(make_rug(3, 5, '$'))  # Expected: ["$$$$$", "$$$$$", "$$$$$"]
print(make_rug(2, 2, 'A'))  # Expected: ["AA", "AA"]