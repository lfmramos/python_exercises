from typing import List

"""
Given two arrays of strings list1 and list2, find the common strings with the least index sum.

A common string is a string that appeared in both list1 and list2.

A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.

Return all the common strings with the least index sum. Return the answer in any order.
"""
class Solution:
    def findCommonStrings(self, list1, list2):
        # Initialize a hash map to store the indices of strings in list2
        list2_indices = {string: index for index, string in enumerate(list2)}
        
        # Initialize variables to store the minimum index sum and the result list
        min_index_sum = float('inf')
        result = []
        
        # Iterate over the strings in list1
        for i, string in enumerate(list1):
            # If the string is also in list2
            if string in list2_indices:
                # Calculate the index sum
                index_sum = i + list2_indices[string]
                
                # If the index sum is less than the current minimum, update the result list
                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    result = [string]
                # If the index sum is equal to the current minimum, append the string to the result list
                elif index_sum == min_index_sum:
                    result.append(string)
        
        # Return the common strings with the minimum index sum
        return result

# Example usage:
# sol = Solution()
# print(sol.findCommonStrings(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))  # Output: ["Shogun"]