"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""

class Solution:
    def firstUniqueChar(self, s: str) -> int:
        # Dictionary to store the frequency of each character
        character_frequency = {}
        
        # First pass: count the frequency of each character in the string
        for letter in s:
            # Increment the count for the character in the dictionary
            character_frequency[letter] = character_frequency.get(letter, 0) + 1
        
        # Second pass: find the first character with a frequency of 1
        for index, letter in enumerate(s):
            # Check if the character's frequency is 1
            if character_frequency[letter] == 1:
                # Return the index of the first unique character
                return index
        
        # If no unique character is found, return -1
        return -1

# Example usage:
# sol = Solution()
# print(sol.firstUniqueChar("leetcode"))  # Output: 0
# print(sol.firstUniqueChar("loveleetcode"))  # Output: 2
# print(sol.firstUniqueChar("aabb"))  # Output: -1