class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        remainders = {}
        # go through, get the remainder and the index

        for i, num in enumerate(nums):
            remainder = target - num

            if num in remainders:
                output = [remainders[num],i]
                return output

            remainders[remainder] = i
            
        