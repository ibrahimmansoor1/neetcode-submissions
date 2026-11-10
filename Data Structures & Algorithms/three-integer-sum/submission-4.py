class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #creating a list for the results and sorting the input array
        res = []
        nums.sort()

        # Fix 'a' as the first number of our triplet
        # Example: in [-4, -1, -1, 0, 1, 2], 'a' locks in -4 first, then -1, etc.
        for i, a in enumerate(nums):

            # Skip duplicate values for 'a' so we don't generate the same triplets twice.
            # 'i > 0' prevents checking nums[-1] (the end of the list) on the very first loop.
            # Example: at index 1 (a = -1), it runs. At index 2 (a = -1), a == nums[1] is True, so it skips.
            # when i is 0 so python skips it cuz its False and it skips the continue and runs the loop normally
            if i > 0 and a == nums[i - 1]:
                continue
            
            #2 pointers creation 
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                # sum of 3 bigger than 0 so right moves behind and vice versa
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])

                    # Move the left pointer forward to keep searching 
                    # for other valid pairs with the same a
                    l += 1

                    # Skip duplicate values for 'l' to avoid adding the exact same triplet twice,
                    # while ensuring 'l' does not cross past 'r'.
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res




        