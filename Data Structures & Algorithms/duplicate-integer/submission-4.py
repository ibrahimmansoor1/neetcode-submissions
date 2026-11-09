class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        newset = set()

        for n in nums:
            if n in newset:
                return True
        
            

            newset.add(n)

        return False 

        
          


        