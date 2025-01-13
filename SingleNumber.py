class Solution:
    def singleNumber(self, nums) -> int:
        # Initialize result to 0
        result = 0
        
        # Iterate through each number in the list
        for num in nums:
            # Apply XOR operation between result and the current number
            # XORing a number with itself results in 0
            # XORing a number with 0 results in the number itself
            # This will cancel out all numbers that appear twice, leaving only the single number
            result ^= num
        
        # Return the single number that appears only once
        return result

# Example usage:
# sol = Solution()
# print(sol.singleNumber([2, 2, 1]))  # Output: 1
# print(sol.singleNumber([4, 1, 2, 1, 2]))  # Output: 4
# print(sol.singleNumber([1]))  # Output: 1