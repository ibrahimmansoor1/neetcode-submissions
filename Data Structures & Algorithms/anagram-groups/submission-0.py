class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        result = defaultdict(list) #mapping character count to list of anagrams

        for s in strs:
            count = [0] * 26 #a to z
            for c in s:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s)
        return list(result.values())
