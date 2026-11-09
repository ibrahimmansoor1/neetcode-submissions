class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        #we use a set since values cant be repeated
        #Initialise a set where we add values to it
        #When the value is not present it should be false
        #When the valuse is present it should be true

        hashset = set()

        for n in nums:            # Loops through array
            if n in hashset:      # Checks in the list 
                return True       # Checks if there is a duplicate
            hashset.add(n)        # If not then it adds the n in the hashset
        return False              # Returns false