"""
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

- 0 <= i, j, k, l < n
- nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
"""

class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        # Create a dictionary to store the sum of pairs of nums1 and nums2
        sum_count = {}
        
        # Count the number of tuples that sum to zero
        count = 0
        
        # Calculate all possible sums of pairs from nums1 and nums2
        for num1 in nums1:
            for num2 in nums2:
                sum_count[num1 + num2] = sum_count.get(num1 + num2, 0) + 1
        
        # Calculate all possible sums of pairs from nums3 and nums4
        # and check if the negative of the sum exists in the dictionary
        for num3 in nums3:
            for num4 in nums4:
                count += sum_count.get(-(num3 + num4), 0)
        
        return count

# Example usage:
sol = Solution()
print(sol.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))  # Expected output: 2