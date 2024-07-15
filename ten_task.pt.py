# Multi-level Cache System Simulation
# Objective: Design a class `CacheSystem` that simulates a two-level cache (L1 and L2). L1 cache has faster access but lower capacity than L2.
# Parameters:
# - l1_size: Integer representing the number of entries L1 cache can hold.
# - l2_size: Integer representing the number of entries L2 cache can hold.
# Returns:
# - None; methods will handle cache operations.
# Details:
# - Implement methods for `put` (to add or update data) and `get` (to retrieve data).
# - Use an LRU (Least Recently Used) policy for cache eviction when the cache is full.
# - If an item is accessed from L2, it should be moved to L1 (if there's space, otherwise evict the least recently used item from L1).

# Example usage:
# cache = CacheSystem(2, 3)
# cache.put('a', 1)
# cache.put('b', 2)
# cache.get('a')  # Expected to access from L1
# cache.put('c', 3)
# cache.put('d', 4)  # Should trigger eviction in L2, moving 'c' to L1, evicting 'b'
# cache.get('b')  # Expected: None
# cache.get('c')  # Expected to move from L1, 'd' remains in L2

class CacheSystem:
    def __init__(self, l1_size, l2_size):
        self.l1_size = l1_size
        self.l2_size = l2_size
        self.l1 = {}
        self.l2 = {}

    def put(self, key, value):
        if key in self.l1:
            self.l1.pop(key)
        elif key in self.l2:
            self.l2.pop(key)
        elif len(self.l1) == self.l1_size:
            self.l1.pop(next(iter(self.l1)))
        self.l1[key] = value

    def get(self, key):
        if key in self.l1:
            return self.l1[key]
        elif key in self.l2:
            value = self.l2.pop(key)
            self.l1[key] = value
            return value
        return None

# Example usage:
cache = CacheSystem(2, 3)
cache.put('a', 1)
cache.put('b', 2)
print(cache.get('a'))  # Expected to access from L1
cache.put('c', 3)
cache.put('d', 4)  # Should trigger eviction in L2, moving 'c' to L1, evicting 'b'
print(cache.get('b'))  # Expected: None
print(cache.get('c'))  # Expected to move from L1, 'd' remains in L2

