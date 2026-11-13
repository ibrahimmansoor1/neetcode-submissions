class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #creating a count hashmap
        res = 0 #max length initialised to 0
        # left pointer at 0
        l = 0
        
        # right pointer iterating
        for r in range(len(s)):
            # adding the character at right to the hashmap
            count[s[r]] = 1 + count.get(s[r], 0)
            # while lenght of the window - most frequent set is bigger than k
            while (r - l + 1) - max(count.values()) > k:
                # we remove the last character from the count so the left pointer also moves and the count of the character gets decreased
                count[s[l]] -= 1
                # the left pointer gets updated 
                l += 1
            #result is the max
            res = max(res, (r - l + 1))
        return res

        #for a constant time approach we add max f