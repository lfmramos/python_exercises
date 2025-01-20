"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
such that nums[i] == nums[j] and abs(i - j) <= k.
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the index of each element
        index_map = {}
        
        # Iterate over the elements of the array
        for i, num in enumerate(nums):
            # Check if the element is already in the dictionary
            if num in index_map:
                # Check if the difference between the indices is less than or equal to k
                if i - index_map[num] <= k:
                    return True
            # Update the index of the element in the dictionary
            index_map[num] = i
        
        return False