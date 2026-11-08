class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c =='[':
                stack.append(']')
            else:
                if len(stack) == 0:
                    return False
                stackPop = stack.pop()
                if stackPop != c:
                    return False
        if len(stack) > 0:
            return False
        return True
