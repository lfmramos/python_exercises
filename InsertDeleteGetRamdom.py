"""
Implement the RandomizedSet class:

- RandomizedSet() Initializes the RandomizedSet object.
- bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
- bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
- int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
"""
class RandomizedSet:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Dictionary to store the value to index mapping
        self.val_to_index = {}
        # List to store the values
        self.values = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        # If the value is already in the set, return False
        if val in self.val_to_index:
            return False
        # Add the value to the dictionary with its index in the list
        self.val_to_index[val] = len(self.values)
        # Append the value to the list
        self.values.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # If the value is not in the set, return False
        if val not in self.val_to_index:
            return False
        # Get the index of the value to be removed
        index = self.val_to_index[val]
        # Get the last value in the list
        last_val = self.values[-1]
        # Move the last value to the index of the value to be removed
        self.values[index] = last_val
        self.val_to_index[last_val] = index
        # Remove the last value from the list
        self.values.pop()
        # Delete the value from the dictionary
        del self.val_to_index[val]
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # Return a random element from the list
        return random.choice(self.values)

# Example usage:
# randomizedSet = RandomizedSet()
# print(randomizedSet.insert(1))  # Output: True
# print(randomizedSet.remove(2))  # Output: False
# print(randomizedSet.insert(2))  # Output: True
# print(randomizedSet.getRandom())  # Output: 1 or 2
# print(randomizedSet.remove(1))  # Output: True
# print(randomizedSet.insert(2))  # Output: False
# print(randomizedSet.getRandom())  # Output: 2