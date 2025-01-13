"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        # Helper function to compute the sum of the squares of the digits of a number
        def get_next(number):
            total_sum = 0
            while number > 0:
                digit = number % 10  # Get the last digit
                total_sum += digit * digit  # Add the square of the digit to the total sum
                number //= 10  # Remove the last digit
            return total_sum
        
        seen = set()  # Initialize a set to keep track of seen numbers
        while n != 1 and n not in seen:  # Continue until n equals 1 or a cycle is detected
            seen.add(n)  # Add the current number to the set of seen numbers
            n = get_next(n)  # Update n to the next number in the sequence
        
        return n == 1  # Return True if n equals 1, indicating a happy number

# Example usage:
# sol = Solution()
# print(sol.isHappy(19))  # Output: True
# print(sol.isHappy(2))   # Output: False