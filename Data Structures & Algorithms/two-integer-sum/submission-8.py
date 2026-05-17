class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            remainder = target - num
            if remainder not in seen:
                seen[num] = i
            else:
                output = [seen[remainder], i]
                return output