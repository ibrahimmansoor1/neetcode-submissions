class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # array res = [1,1,1,1]
        res = [1] * (len(nums))
         
        # prefix whee it loops through nums  and starts multiplying it w nums
        # end looks like with example [1,2,3,4]
        # [1,1,1,1]
        # [1,1,1,1]
        # [1,1,1,1]

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]


        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


         