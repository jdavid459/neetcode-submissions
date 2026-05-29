class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, num in enumerate(nums):
            remainder = target - num
            if num not in seen:
                seen[remainder] = i
            else:
                return [seen[num], i]

        