"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have.
Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Create a set of jewels for faster lookup
        jewel_set = set(jewels)
        
        # Count the number of stones that are also jewels
        count = 0
        for stone in stones:
            if stone in jewel_set:
                count += 1
        
        return count
    
# Example usage:
# sol = Solution()
# print(sol.numJewelsInStones("aA", "aAAbbbb"))  # Output: 3
# print(sol.numJewelsInStones("z", "ZZ"))  # Output: 0
# print(sol.numJewelsInStones("abc", "ABC"))  # Output: 0
# print(sol.numJewelsInStones("abc", "abc"))  # Output: 3