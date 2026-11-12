class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characterSet = set()
        l = 0
        res = 0
        
        #initialised right pointer here
        for r in range(len(s)):
            # if the character at right pointer is in the set, we remove it from the set
            # [a,b,c,a] and at a its a repetition so we remove a from the set 
            while s[r] in characterSet:
                characterSet.remove(s[l])
                # the left pointer is updated then
                l += 1
            # this is the first point where characters are added/
            characterSet.add(s[r])
            res = max(res, r - l + 1)
        return res        