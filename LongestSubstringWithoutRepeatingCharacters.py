"""
Given a string s, find the length of the longest substring without repeating characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a dictionary to store the index of the last occurrence of each character
        last_occurrence = {}
        
        # Initialize the start of the window and the length of the longest substring
        start = 0
        max_length = 0
        
        # Iterate through the string
        for i, char in enumerate(s):
            # If the character is a repeat, update the start of the window
            if char in last_occurrence and last_occurrence[char] >= start:
                start = last_occurrence[char] + 1
            
            # Update the last occurrence of the character
            last_occurrence[char] = i
            
            # Update the length of the longest substring
            max_length = max(max_length, i - start + 1)
        
        return max_length