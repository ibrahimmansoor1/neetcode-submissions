class Solution:

    def encode(self, strs: List[str]) -> str:

        #for decoding add a string from strs in the format 4#neet4#love
        #s iterates in strs and we add to the results
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:

        #i tells what position we are at in the input string
        res, i = [], 0

        while i < len(s):
            j = i

            # while the string at j is not equal to j
            while s[j] != '#':
                j += 1
            length = int(s[i: j]) # i to j not j since i to j is the number integer
            res.append(s[j + 1: j + 1 + length])
            
            #now we update i

            i = j + 1 + length

        return res





