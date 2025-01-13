
"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
class Solution:
    def containsDuplicate(self, nums) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Example usage:
# sol = Solution()
# print(sol.containsDuplicate([1, 2, 3, 1]))  # Output: True
# print(sol.containsDuplicate([1, 2, 3, 4]))  # Output: False