# Implement a Custom Iterator for Prime Numbers
# Objective: Design a class `PrimeIterator` that generates an infinite sequence of prime numbers.
# Parameters:
# - None, but the iterator should handle internal state for generating primes.
# Returns:
# - Prime numbers, one at a time, indefinitely.
# Details:
# - Implement the iterator protocol methods `__iter__()` and `__next__()`.
# - Use a sophisticated method to check for primes to ensure efficiency as numbers grow large.

class PrimeIterator:
    pass

# Example:
# primes = PrimeIterator()
# for _ in range(10):
#     print(next(primes))  # Prints the first 10 prime numbers

class PrimeIterator:
    def __init__(self):
        self.primes = [2]
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        while not self.is_prime(self.current):
            self.current += 1
        self.primes.append(self.current)
        return self.current

    def is_prime(self, n):
        for prime in self.primes:
            if n % prime == 0:
                return False
        return True

primes = PrimeIterator()
for _ in range(10):
    print(next(primes))  # Prints the first 10 prime numbers
