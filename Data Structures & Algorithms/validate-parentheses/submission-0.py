class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"}" : "{", ")" : "(", "]" : "["}


        for c in s:        
            # the first if is for opening ones which are added to the stack like this (
            if c in closeToOpen:
                # this is for closing ones which if found they are removed like )
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

        