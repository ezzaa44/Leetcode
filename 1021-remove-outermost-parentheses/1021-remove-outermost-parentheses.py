class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        stack = []
        for i in s:
            if len(stack) == 0 :
                stack.append(i)
                continue      
            if i == ')' and len(stack) == 1:
                stack.pop()
                continue
            if i == ')':
                stack.pop()
                result.append(i)
            if i == '(':
                stack.append(i)
                result.append(i)
        
        return ''.join(result)
