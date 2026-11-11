class Solution:
    def maxArea(self, height: list[int]) -> int:

        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height [r]:
                l += 1
            #elif height[l] > height [r]:                 # we can leave this out since 
            #    r -= 1                                     the next else does the exact same thing
            else:
                r -= 1
        return res

        