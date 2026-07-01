class Solution:
    def isBalanced(self, s):
        # code here
        stack = []
        pairs = {
            ']':'[',
            ')':'(',
            '}':'{'
        }
        
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack[-1] != pairs[ch]:
                    return False
                
                stack.pop()
        return len(stack)==0
            
        
