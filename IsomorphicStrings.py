"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Dictionaries to store the character mappings
        s_to_t = {}
        t_to_s = {}
        
        # Iterate over the characters of both strings
        for char_s, char_t in zip(s, t):
            # Check if there is a conflicting mapping from s to t
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t
            
            # Check if there is a conflicting mapping from t to s
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s
        
        # If no conflicts are found, the strings are isomorphic
        return True

sol = Solution()
print(sol.isIsomorphic("badc", "baba"))

# Example usage:
# sol = Solution()
# print(sol.isIsomorphic("egg", "add"))  # Output: True
# print(sol.isIsomorphic("foo", "bar"))  # Output: False
# print(sol.isIsomorphic("paper", "title"))  # Output: True