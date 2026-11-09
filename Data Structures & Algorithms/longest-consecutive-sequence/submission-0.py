class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        #creating a set where we put nums and initialising longest sequence to 0
        numSet = set(nums)
        longestsequence = 0
        
        #iterating through the nums list
        for num in nums:
            #if a number does not have a number that comes before it (99 is before 100,so added 
            #                                                         but 3 is there before 4 so not added)
            if (num - 1) not in numSet:
                #length of sequence for 100 is set to 1 and for 4 its not
                length = 1
            
                # (1+1 = 2) is in subset so the lenght is 2 now, but for 100 there is nothing so its length is 1
                while (num + length) in numSet:
                    length += 1
                longestsequence = max(length, longestsequence)

        return longestsequence

        