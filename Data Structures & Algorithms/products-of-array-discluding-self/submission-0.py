class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # nums = [1,2,4,6]
        # for i = 0, run inner loop j, loop through the rest multiplying each, output the value
        # but then we have to get indexes before as well, so we really need to like pop out a number, keep the rest of the list
        # and loop through the remainders for that index output


        # [1,x,4,6]
        # save list of all except nums[i]
        # multiple the rest...that'd be n*n I think n2 time complexity

        products = []
        for i, num in enumerate(nums): #loop through nums
            product = 1

            # remainder = nums.remove(nums[i]) #create new list with all but the number at index
            for j in range(len(nums)): #then loop through the remainder array
                if j == i:
                    continue
                product *= nums[j] # add/multiple each
            products.append(product)
        return products

            

        