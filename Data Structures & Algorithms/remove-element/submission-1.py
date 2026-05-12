class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_filtered = []

        for num in nums:
            if num == val:
                pass
            else:
                nums_filtered.append(num)
            # return nums_filtered
        
        # i = 0 
        # result = []

        # while i < len(nums_filtered):
        #     for num in nums:
        #         if num == val:
        #             pass
        #         else:
        #             result.append(num)
        #             i += 1

        for i in range(len(nums_filtered)):
            nums[i] = nums_filtered[i]

        return len(nums_filtered)

