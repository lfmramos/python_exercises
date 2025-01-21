"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK = {}
        for num in nums:
            if num in topK:
                topK[num] += 1
            else:
                topK[num] = 1
        sorted_topK = sorted(topK.items(), key=lambda x: x[1], reverse=True)
        return [key for key, value in sorted_topK[:k]]
# Time complexity: O(n log n) where n is the array's size
# Space complexity: O(n) where n is the array's size
