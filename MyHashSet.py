class MyHashSet:
    def __init__(self):
        # Initialize the size of the hash set
        self.size = 1000
        # Create a list of empty lists (buckets) to store the keys
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        # Compute the bucket index for the given key using modulo operation
        return key % self.size

    def add(self, key):
        # Get the bucket index for the key
        bucket_index = self._hash(key)
        # If the key is not already in the bucket, add it
        if key not in self.buckets[bucket_index]:
            self.buckets[bucket_index].append(key)

    def remove(self, key):
        # Get the bucket index for the key
        bucket_index = self._hash(key)
        # If the key is in the bucket, remove it
        if key in self.buckets[bucket_index]:
            self.buckets[bucket_index].remove(key)

    def contains(self, key):
        # Get the bucket index for the key
        bucket_index = self._hash(key)
        # Return True if the key is in the bucket, otherwise False
        return key in self.buckets[bucket_index]

# Example usage:
# myHashSet = MyHashSet()
# myHashSet.add(1)  # Add key 1 to the hash set
# myHashSet.add(2)  # Add key 2 to the hash set
# print(myHashSet.contains(1))  # Check if key 1 is in the hash set, returns True
# print(myHashSet.contains(3))  # Check if key 3 is in the hash set, returns False
# myHashSet.add(2)  # Add key 2 to the hash set again (no effect since 2 is already present)
# print(myHashSet.contains(2))  # Check if key 2 is in the hash set, returns True
# myHashSet.remove(2)  # Remove key 2 from the hash set
# print(myHashSet.contains(2))  # Check if key 2 is in the hash set, returns False