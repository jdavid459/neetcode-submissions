class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #brute force
        #sort array
        #longest=1
        #loop through array
        #if i=0, continue, elsif nums[i]+1 == nums[i+1] then longest +=1

        if len(nums) == 0:
            return 0
        nums_sorted = sorted(nums)
        #2,3,4,4,5,10,20
        

        current = 1
        longest = 1
        for i, num in enumerate(nums_sorted):
            if i == 0:
                continue
            
            if nums_sorted[i] == nums_sorted[i - 1]:
                continue

            elif nums_sorted[i] == nums_sorted[i - 1] + 1:
                current += 1
                longest = max(longest, current)

            else:
                current = 1
        return longest
