"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
"""
class Solution:
    def intersection(self, nums1, nums2):
        # Create sets from the input lists to remove duplicates
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Find the intersection of the two sets
        result_set = set1.intersection(set2)
        
        # Convert the result set to a list
        result = list(result_set)
        
        return result

# Example usage:
# sol = Solution()
# print(sol.intersection([1, 2, 2, 1], [2, 2]))  # Output: [2]
# print(sol.intersection([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [9, 4]