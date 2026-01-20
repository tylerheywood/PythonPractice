# https://leetcode.com/problems/two-sum/
'''
Problem:
Return indices of two numbers such that they add up to the target.

Approach:
- Iterate once through the list
- Store each number with its index in a dictionary
- For each number, calculate the required pair_value (target - num)
- If the pair_value has already been seen, return both indices immediately

Why this works:
- Dictionary lookups are O(1)
- Each element is processed once → O(n) time
- Avoids nested loop
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i, num in enumerate(nums):

            pair_value = target - num
            if pair_value in index_map:
                return [index_map[pair_value], i]

            index_map[num] = i
        return index_map

tyler = Solution()

print(tyler.twoSum(nums=[2, 7, 11, 15], target=9))

