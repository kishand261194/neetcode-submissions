class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        res = True
        
        if len(s)%2 !=0:
            return False

        for i in s :
            if i in ['(','[','{']:
                stack.append(i)

            if i in [')',']','}']:
                c = None
                if (len(stack) > 0):
                    c = stack.pop()
                if i == ')':
                    if c != '(':
                        res = False
                        break
                if i == ']':
                    if c != '[':
                        res = False
                        break
                if i == '}':
                    if c != '{':
                        res = False
                        break

        if len(stack) != 0:
            return False
        return res
