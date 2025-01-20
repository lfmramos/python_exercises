"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to store the sorted strings and their anagrams
        anagrams = {}
        
        # Iterate over the strings in the input list
        for string in strs:
            # Sort the characters of the string
            sorted_string = ''.join(sorted(string))
            
            # Add the string to the dictionary based on the sorted characters
            if sorted_string in anagrams:
                anagrams[sorted_string].append(string)
            else:
                anagrams[sorted_string] = [string]
        
        # Return the values of the dictionary as the grouped anagrams
        return list(anagrams.values())