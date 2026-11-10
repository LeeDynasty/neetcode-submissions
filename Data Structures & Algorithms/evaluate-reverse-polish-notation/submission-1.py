class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token in operators:
                result = None
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if token == '+':
                    result = num1 + num2
                elif token == '-':
                    result = num1 - num2
                elif token == '*':
                    result = num1 * num2
                else:
                    result = num1 / num2
                
                stack.append(result)
            else:
                stack.append(token)
        
        return int(stack.pop())