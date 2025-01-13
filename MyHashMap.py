class MyHashMap:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Use a Python dictionary to store key-value pairs
        self.hashmap = {}

    def put(self, key: int, value: int) -> None:
        """
        Insert a (key, value) pair into the HashMap. If the key already exists, update the value.
        value will always be non-negative.
        """
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
        """
        return self.hashmap.get(key, -1)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key.
        """
        if key in self.hashmap:
            del self.hashmap[key]

# Example usage:
# obj = MyHashMap()
# obj.put(1, 1)  # Insert key 1 with value 1
# obj.put(2, 2)  # Insert key 2 with value 2
# print(obj.get(1))  # Returns 1, the value associated with key 1
# print(obj.get(3))  # Returns -1, as key 3 is not present
# obj.put(2, 1)  # Update the value for key 2 to 1
# print(obj.get(2))  # Returns 1, the updated value for key 2
# obj.remove(2)  # Remove the mapping for key 2
# print(obj.get(2))  # Returns -1, as key 2 has been removed