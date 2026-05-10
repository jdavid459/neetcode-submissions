class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #nums = [3,4,5,6], target = 7


        # 3: 0
        # 4: 1
        # 5: 2
        # 6: 3

        d = {}
        for i, num in enumerate(nums):
            remainder = target - num
            
            if remainder in d:
                return [d[remainder],i]

            d[num] = i
            
            

        