"""
Given two integer arrays nums1 and nums2, return an array of their intersection.

Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""

class Solution:
    def intersect(self, nums1, nums2):
        # Ensure nums1 is the smaller array to optimize space complexity
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # Dictionary to store the frequency of each element in the smaller array
        intersection = {}
        
        # Count the frequency of each element in the smaller array
        for num in nums1:
            intersection[num] = intersection.get(num, 0) + 1
        
        # List to store the result of the intersection
        result = []
        
        # Find the intersection elements in the larger array
        for num in nums2:
            if num in intersection and intersection[num] > 0:
                result.append(num)
                intersection[num] -= 1
        
        return result

# Example usage:
sol = Solution()
print(sol.intersect([1, 2, 2, 1], [2, 2]))  # Output: [2, 2]
print(sol.intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [4, 9] or [9, 4]