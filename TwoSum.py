"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the value and its index
        num_to_index = {}
        
        # Iterate over the list of numbers
        for index, num in enumerate(nums):
            # Calculate the complement that would add up to the target
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                # If found, return the indices of the current number and the complement
                return [num_to_index[complement], index]
            
            # If not found, add the current number and its index to the dictionary
            num_to_index[num] = index
        
        # Return None if no solution is found (though the problem guarantees one solution)
        return None